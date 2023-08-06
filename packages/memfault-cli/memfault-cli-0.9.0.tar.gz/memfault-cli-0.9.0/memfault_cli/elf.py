import pathlib
from typing import BinaryIO, Iterable, Optional

import more_itertools
from elftools.construct import Container
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import NoteSection
from elftools.elf.segments import NoteSegment

# FIXME: Deduplicate. Copy pasta from elf_utils.py

NT_GNU_BUILD_ID = "NT_GNU_BUILD_ID"

ELF_NOTE_SECTION_OWNER_GNU = "GNU"


def is_elf(file: BinaryIO) -> bool:
    original_offset = file.tell()
    magic = file.read(4)
    file.seek(original_offset)
    return magic == b"\x7FELF"


def elf_has_debug_info(elf: ELFFile) -> bool:
    # Note: not using .has_dwarf_info() because it will return True if .eh_frame is present.
    # This section is usually kept in stripped binaries, because certain languages (C++) depend on it at runtime.
    return bool(elf.get_section_by_name(".debug_info") or elf.get_section_by_name(".zdebug_info"))


def find_elf_files(dir: pathlib.Path, *, recurse: bool = True) -> Iterable[pathlib.Path]:
    if not dir.is_dir() or not dir.exists():
        return
    for path in dir.iterdir():
        if path.is_dir() and recurse:
            yield from find_elf_files(path)
        elif path.is_file():
            with open(path, "rb") as f:
                if not is_elf(f):
                    continue
            yield path


def get_note_segments(elf: ELFFile) -> Iterable[NoteSegment]:
    return filter(lambda segment: isinstance(segment, NoteSegment), elf.iter_segments())


def get_note_sections(elf: ELFFile) -> Iterable[NoteSection]:
    return filter(lambda segment: isinstance(segment, NoteSection), elf.iter_sections())


def get_notes(elf: ELFFile) -> Iterable[Container]:
    for note_segment in get_note_segments(elf):
        yield from note_segment.iter_notes()
    for note_section in get_note_sections(elf):
        yield from note_section.iter_notes()


def is_gnu_build_id_note_section(section: NoteSection) -> bool:
    return (section.n_type == NT_GNU_BUILD_ID) and (section.n_name == ELF_NOTE_SECTION_OWNER_GNU)


def get_gnu_build_id(elf: ELFFile) -> Optional[str]:
    build_id_note = more_itertools.first_true(
        get_notes(elf),
        pred=is_gnu_build_id_note_section,
    )
    if not build_id_note:
        return None
    return build_id_note.n_desc
