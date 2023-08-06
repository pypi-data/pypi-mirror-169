import dataclasses
import logging
import pathlib
from typing import Dict, Iterable, TextIO, Tuple

import more_itertools

from .elf import find_elf_files

# See https://docs.yoctoproject.org/overview-manual/concepts.html#package-splitting
# for the directory structure of the Yocto build output.

LOG = logging.getLogger(__name__)


@dataclasses.dataclass
class ManifestEntry:
    package: str  # Note this is the name *after* package splitting!
    arch: str
    version: str

    @staticmethod
    def from_line(line: str) -> "ManifestEntry":
        components = line.split(maxsplit=3)
        assert len(components) == 3, "Manifest line has unexpected number of items"
        return ManifestEntry(*components)


def parse_image_manifest(file: Iterable[str]) -> Iterable[ManifestEntry]:
    for line in file:
        yield ManifestEntry.from_line(line)


def tmp_path_from_manifest(manifest: TextIO) -> pathlib.Path:
    """
    This function returns the resolved tmp/ given a .manifest file's path.
    The .manifest file is created by Yocto in tmp/deploy/images/<arch>/.
    """
    manifest_path = pathlib.Path(manifest.name).resolve()
    return manifest_path.parent.parent.parent.parent


def gather_workdirs_by_split_package_names_and_version(
    arch_path: pathlib.Path,
) -> Dict[Tuple[str, str], pathlib.Path]:
    """
    The manifest file holds package names *after* splitting. We need to map these back to the paths where each was
    built ("image" folder). The folder for each package before splitting has a "packages-split" folder. In this
    folder, there are subfolders named after the packages *after* splitting.
    The directory structure in the arch path looks like this:
    - cortexa57-poky-linux  <- arch_path
        - PN (package name before splitting)
            - PV-PR (version - revision) <- package's WORKDIR
                - image <- folder containing "raw" .elfs (symbols)
                - packages-split
                    - PN-1 (packages name after splitting()
                    - PN-2
                    - PN..
    :param arch_path: The arch path to search in.
    :return: Dict mapping (package name after splitting, package version) => package's WORKDIR
    """
    mapping = {}

    for package_dir in arch_path.iterdir():
        for package_workdir in package_dir.iterdir():
            packages_split_dir = package_workdir / "packages-split"
            if not packages_split_dir.exists():
                mapping[(package_dir.name, package_workdir.name)] = package_workdir
                continue
            for dir in packages_split_dir.iterdir():
                mapping[(dir.name, package_workdir.name)] = package_workdir

    return mapping


def find_package_workdirs_from_image_manifest_entries(
    entries: Iterable[ManifestEntry], tmp_path: pathlib.Path
) -> Iterable[pathlib.Path]:
    """
    This function finds package folders matching the given manifest file.
    :return: Iterable with found package WORKDIRs.
    """
    entries_by_arch = more_itertools.map_reduce(entries, lambda e: e.arch)
    work_path = tmp_path / "work"
    if not work_path.exists():
        raise FileNotFoundError(
            f"Missing {work_path}. The .manifest file is expected to "
            f"be in the location where it was originally put by Yocto."
        )
    for arch_path in work_path.iterdir():
        if not arch_path.is_dir():
            continue
        workdir_by_package_name_and_version = gather_workdirs_by_split_package_names_and_version(
            arch_path
        )
        arch, _, _ = arch_path.name.partition("-")
        entries_for_arch = entries_by_arch.get(arch)
        if not entries_for_arch:
            LOG.debug("No manifest entries from arch: %s", arch)
            continue
        for entry in entries_for_arch:
            package_workdir = workdir_by_package_name_and_version.get(
                (entry.package, entry.version)
            )
            if package_workdir:
                yield package_workdir
            else:
                LOG.debug("Could not find package workdir for %s", entry)


def should_ignore_elf(rel_elf_path: pathlib.Path) -> bool:
    # Ignore ptests -- See https://wiki.yoctoproject.org/wiki/Ptest
    if rel_elf_path.suffix in {".a", ".o"}:
        LOG.debug("Ignoring %s (static lib / object file)", rel_elf_path)
        return True
    if any((parent.name == "ptest" for parent in rel_elf_path.parents)):
        LOG.debug("Ignoring %s (ptest)", rel_elf_path)
        return True
    return False


def should_ignore_package(entry: ManifestEntry) -> bool:
    _, _, ending = entry.package.rpartition("-")
    if ending.startswith("locale-"):
        # Ignore all *-locale-* packages (optimization).
        return True
    return ending in {
        # Ignored because they contain split .elf files (only .debug_info and no .text/.data):
        "dbg",
        # Ignored because they contain static libraries, not executables:
        "staticdev",
        # Ignored because they contain test executables:
        "ptest",
        # Ignore source, doc and locale packages (optimization):
        "src",
        "doc",
        "locale",
    }


def find_elf_files_from_image_manifest(manifest: TextIO) -> Iterable[pathlib.Path]:
    entries = (e for e in parse_image_manifest(manifest) if not should_ignore_package(e))
    tmp_path = tmp_path_from_manifest(manifest)
    for workdir in more_itertools.unique_everseen(
        find_package_workdirs_from_image_manifest_entries(entries, tmp_path)
    ):
        for elf_file in find_elf_files(workdir / "image"):
            if should_ignore_elf(elf_file.relative_to(workdir)):
                continue
            yield elf_file
