import dataclasses
import logging
import pathlib
import tarfile
import tempfile
from typing import Dict, Iterable

from .elf import ELFFileInfo, find_elf_files

# See https://docs.yoctoproject.org/overview-manual/concepts.html#package-splitting
# for the directory structure of the Yocto build output.

LOG = logging.getLogger(__name__)


def tmp_path_from_image(image: pathlib.Path) -> pathlib.Path:
    """
    This function returns the resolved tmp/ given a .manifest file's path.
    The .manifest file is created by Yocto in tmp/deploy/images/<arch>/.
    """
    return image.resolve().parent.parent.parent.parent


def non_native_package_paths(tmp_path: pathlib.Path) -> Iterable[pathlib.Path]:
    """Optimzation: skip *-native packages when searching for symbol files"""
    for arch_dir in (tmp_path / "work").iterdir():
        for pn_dir in arch_dir.iterdir():
            if pn_dir.name.endswith("-native"):
                continue
            yield pn_dir


def find_elf_files_from_non_native_packages(tmp_path: pathlib.Path) -> Iterable[ELFFileInfo]:
    for package_path in non_native_package_paths(tmp_path):
        yield from find_elf_files(package_path)


def should_ignore_elf(elf_info: ELFFileInfo) -> bool:
    if elf_info.path.suffix in {".a", ".o"}:
        LOG.debug("Ignoring %s (static lib / object file)", elf_info.path)
        return True
    # Ignore ptests -- See https://wiki.yoctoproject.org/wiki/Ptest
    if any((parent.name == "ptest" for parent in elf_info.path.parents)):
        LOG.debug("Ignoring %s (ptest)", elf_info.path)
        return True
    if elf_info.gnu_build_id is None:
        LOG.debug("Ignoring %s (GNU Build ID missing)", elf_info.path)
        return True
    if not elf_info.has_text:
        LOG.debug("Ignoring %s (.text missing)", elf_info.path)
        return True
    return False


@dataclasses.dataclass
class FindSymbolFilesResult:
    found: Iterable[ELFFileInfo]
    missing: Iterable[ELFFileInfo]


def find_symbol_files_to_upload(
    *, image_elfs: Iterable[ELFFileInfo], tmp_work_elfs: Iterable[ELFFileInfo]
) -> FindSymbolFilesResult:
    symbols_by_build_id: Dict[str, ELFFileInfo] = {}
    missing_debug_info_by_build_id: Dict[str, ELFFileInfo] = {}

    # First, analyze all the .elfs in the image:
    for elf_info in image_elfs:
        if should_ignore_elf(elf_info):
            continue
        gnu_build_id = elf_info.gnu_build_id
        assert gnu_build_id  # Should already be filtered out by should_ignore_elf
        if elf_info.has_debug_info:
            symbols_by_build_id[gnu_build_id] = elf_info
        else:
            missing_debug_info_by_build_id[gnu_build_id] = elf_info

    # Next, go through all of tmp/work to find symbols for the ones we miss:
    missing_build_ids = set(missing_debug_info_by_build_id.keys())
    for elf_info in tmp_work_elfs:
        if not missing_build_ids:
            break  # We're done!

        if not elf_info.has_text or not elf_info.has_debug_info:
            continue  # Need both .debug_info and .text/etc.
        if elf_info.gnu_build_id not in missing_build_ids:
            continue
        symbols_by_build_id[elf_info.gnu_build_id] = elf_info
        missing_build_ids.discard(elf_info.gnu_build_id)

    return FindSymbolFilesResult(
        found=symbols_by_build_id.values(),
        missing=(missing_debug_info_by_build_id[build_id] for build_id in missing_build_ids),
    )


def find_elf_files_from_image(image_tar: pathlib.Path) -> Iterable[ELFFileInfo]:
    with tarfile.open(image_tar, "r:*") as tar, tempfile.TemporaryDirectory() as extraction_path:
        tar.extractall(extraction_path)
        yield from find_elf_files(pathlib.Path(extraction_path))
