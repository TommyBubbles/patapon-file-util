from dataclasses import field, dataclass
from typing import Callable
from .patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponStaticDataClass,
    PataponDynamicDataClass
)


@dataclass
class GXTFileHeader(PataponDataClassHeader, PataponStaticDataClass):
    magic: str = field(metadata={"pos": 0, "type": "s", "size": 0x10})
    file_size: int = field(metadata={"pos": 1, "type": "I"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 0x3})
    offset_1: int = field(metadata={"pos": 3, "type": "I"})
    size_1: int = field(metadata={"pos": 4, "type": "I"})
    offset_2: int = field(metadata={"pos": 5, "type": "I"})
    size_2: int = field(metadata={"pos": 6, "type": "I"})
    offset_3: int = field(metadata={"pos": 7, "type": "I"})
    size_3: int = field(metadata={"pos": 8, "type": "I"})
    image_offset: int = field(metadata={"pos": 9, "type": "I"})
    image_size: int = field(metadata={"pos": 10, "type": "I"})


    def __init__(self):
        super().__init__()


@dataclass
class GXTImageHeader(PataponDataClassHeader, PataponStaticDataClass):
    info_size: int = field(metadata={"pos": 0, "type": "I"})
    size_1: int = field(metadata={"pos": 1, "type": "I", "tag": "image_size"})
    size_2: int = field(metadata={"pos": 2, "type": "I"})
    filler_1: list[int] = field(metadata={"pos": 3, "type": "i", "values": 13})


    def __init__(self):
        super().__init__()


@dataclass
class GXTImageBody(PataponDataClassBody, PataponDynamicDataClass):
    raw_image: bytes = field(metadata={"pos": 0, "type": "s", "tag": "image_size", "tag_type": "size"})


    def __init__(self):
        super().__init__()


@dataclass
class GXTPaletteHeader(PataponDataClassHeader, PataponStaticDataClass):
    info_size: int = field(metadata={"pos": 0, "type": "I"})
    used_size: int = field(metadata={"pos": 1, "type": "I", "tag": "palette_size"})
    total_size: int = field(metadata={"pos": 2, "type": "I"})
    filler_1: list[int] = field(metadata={"pos": 3, "type": "i", "values": 13})


    def __init__(self):
        super().__init__()


@dataclass
class GXTPaletteBody(PataponDataClassBody, PataponDynamicDataClass):
    raw_palette: bytes = field(metadata={"pos": 0, "type": "s", "tag": "palette_size", "tag_type": "size"})


    def __init__(self):
        super().__init__()


@dataclass
class Unknown2Header(PataponDataClassHeader, PataponStaticDataClass):
    filler_1: int = field(metadata={"pos": 0, "type": "i"})
    used_size: int = field(metadata={"pos": 1, "type": "i", "tag": "unk2_used_size"})
    total_size: int = field(metadata={"pos": 2, "type": "i", "tag": "unk2_total_size"})
    filler_2: list[int] = field(metadata={"pos": 3, "type": "i", "values": 13})


    def __init__(self):
        super().__init__()


def get_padding(used: int, total: int) -> int:
    return total - used


@dataclass
class Unknown2Body(PataponDataClassBody, PataponDynamicDataClass):
    fl1: list[float] = field(metadata={"pos": 0, "type": "f", "tag": "unk2_used_size", "tag_type": "hex_size"})
    padding_1: list[None] = field(metadata={"pos": 1, "type": "x", "tag": "unk2_total_size", "tag_type": "func", "func": get_padding, "func_args": {"total": "unk2_total_size", "used": "unk2_used_size"}})
    

    def __init__(self):
        super().__init__()


@dataclass
class Unknown3Body(PataponDataClassBody, PataponStaticDataClass):
    i1: int = field(metadata={"pos": 0, "type": "i"})
    file_name_offset: int = field(metadata={"pos": 1, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 2})
    i2: int = field(metadata={"pos": 3, "type": "i"})
    i3: int = field(metadata={"pos": 4, "type": "i"})
    filler_2: list[int] = field(metadata={"pos": 5, "type": "i", "values": 2})
    i4: int = field(metadata={"pos": 6, "type": "i"})
    i5: int = field(metadata={"pos": 7, "type": "i"})
    i6: int = field(metadata={"pos": 8, "type": "i"})
    i7: int = field(metadata={"pos": 9, "type": "i"})
    i8: int = field(metadata={"pos": 10, "type": "i"})
    i9: int = field(metadata={"pos": 11, "type": "i"})
    filler_3: list[int] = field(metadata={"pos": 12, "type": "i", "values": 2})
    i10: int = field(metadata={"pos": 13, "type": "i"})
    i11: int = field(metadata={"pos": 14, "type": "i"})
    file_name: str = field(metadata={"pos": 15, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_4: list[int] = field(metadata={"pos": 16, "type": "i", "values": 6})


    def __init__(self):
        super().__init__()



@dataclass
class GXT(PataponDynamicDataClass):
    file_header: GXTFileHeader = field(metadata={"pos": 0, "type": "header", "data_size": 0x40})
    image_header: GXTImageHeader = field(metadata={"pos": 1, "type": "header", "data_size": 0x40, "tag": "image"})
    image_body: GXTImageBody = field(metadata={"pos": 2, "type": "body", "tag": "image"})
    palette_header: GXTPaletteHeader = field(metadata={"pos": 3, "type": "header", "data_size": 0x40, "tag": "palette"})
    palette_body: GXTPaletteBody = field(metadata={"pos": 4, "type": "body", "tag": "palette"})
    unk_header_1: PataponStaticDataClass = field(metadata={"pos": 5, "type": "header", "data_size": 0x0, "tag": "unk1"})
    unk_body_1: PataponStaticDataClass = field(metadata={"pos": 6, "type": "body", "data_size": 0x0, "tag": "unk1"})
    unk_header_2: Unknown2Header = field(metadata={"pos": 7, "type": "header", "data_size": 0x40, "tag": "unk2"})
    unk_body_2: Unknown2Body = field(metadata={"pos": 8, "type": "body", "data_size": 0x40, "tag": "unk2"})
    unk_body_3: Unknown3Body = field(metadata={"pos": 9, "type": "body", "data_size": 0x80, "tag": "unk3"})


    def __init__(self):
        super().__init__()