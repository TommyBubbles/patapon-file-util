from dataclasses import field, dataclass
from PIL import Image
from math import sqrt
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    FieldMetadata,
    FieldTag
)
from .func.field_func import difference


@dataclass
class GXTFileHeader(PataponDataClassHeader, PataponStaticDataClass):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x10, encoding="utf-8")})
    file_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    offset_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    size_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    offset_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    size_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    offset_3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    size_3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    image_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    image_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})


@dataclass
class GXTImageHeader(PataponDataClassHeader, PataponStaticDataClass):
    info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    size_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("image_size", "source")]})
    size_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})


@dataclass
class GXTImageBody(PataponDataClassBody, PataponDynamicDataClass):
    raw_image: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 0), "tags": [FieldTag("image_size", "size")]})


@dataclass
class GXTPaletteHeader(PataponDataClassHeader, PataponStaticDataClass):
    info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("palette_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})


@dataclass
class GXTPaletteBody(PataponDataClassBody, PataponDynamicDataClass):
    palette: list[bytes] = field(default_factory=list[bytes], metadata={"meta": FieldMetadata("bytes", 0, size=4, byte_order=">"), "tags": [FieldTag("palette_size", "byte_count")]})


@dataclass
class GXTUnknown1Header(PataponDataClassHeader, PataponStaticDataClass):
    pass


@dataclass
class GXTUnknown1Body(PataponDataClassBody, PataponStaticDataClass):
    pass


@dataclass
class GXTUnknown2Header(PataponDataClassHeader, PataponStaticDataClass):
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("unk2_used_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("unk2_total_size", "source")]})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})


@dataclass
class GXTUnknown2Body(PataponDataClassBody, PataponDynamicDataClass):
    fl1: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 0), "tags": [FieldTag("unk2_used_size", "byte_count")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 1), "tags": [FieldTag("fl1_padding", "size", func=difference, func_params={"first": "unk2_total_size", "second": "unk2_used_size"})]})


@dataclass
class GXTUnknown3Body(PataponDataClassBody, PataponStaticDataClass):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    file_name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=2)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    i4: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    i5: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    i6: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    i7: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    i8: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    i9: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 11)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 12, count=2)})
    i10: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 13)})
    i11: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 14)})
    file_name: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20, encoding="utf-8")})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 16, count=6)})


@dataclass
class GXT(PataponDynamicDataClass):
    file_header: GXTFileHeader = field(default_factory=GXTFileHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40)})
    image_header: GXTImageHeader = field(default_factory=GXTImageHeader, metadata={"meta": FieldMetadata("header", 1, data_size=0x40), "tags": [FieldTag("image", "header")]})
    image_body: GXTImageBody = field(default_factory=GXTImageBody, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("image", "body")]})
    palette_header: GXTPaletteHeader = field(default_factory=GXTPaletteHeader, metadata={"meta": FieldMetadata("header", 3, data_size=0x40), "tags": [FieldTag("palette", "header")]})
    palette_body: GXTPaletteBody = field(default_factory=GXTPaletteBody, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("palette", "body")]})
    unk_header_1: GXTUnknown1Header = field(default_factory=GXTUnknown1Header, metadata={"meta": FieldMetadata("header", 5), "tags": [FieldTag("unk1", "header")]})
    unk_body_1: GXTUnknown1Body = field(default_factory=GXTUnknown1Body, metadata={"meta": FieldMetadata("body", 6), "tags": [FieldTag("unk1", "body")]})
    unk_header_2: GXTUnknown2Header = field(default_factory=GXTUnknown2Header, metadata={"meta": FieldMetadata("header", 7, data_size=0x40), "tags": [FieldTag("unk2", "header")]})
    unk_body_2: GXTUnknown2Body = field(default_factory=GXTUnknown2Body, metadata={"meta": FieldMetadata("body", 8, data_size=0x40), "tags": [FieldTag("unk2", "body")]})
    unk_body_3: GXTUnknown3Body = field(default_factory=GXTUnknown3Body, metadata={"meta": FieldMetadata("body", 9, data_size=0x80)})


#     def decompressed_image(self) -> bytes:
#         image: bytes = self.image_body.raw_image
#         palette: list[bytes] = self.palette_body.palette
#         palette_size: int = len(palette)
        
#         result_image: bytes = b''
#         if palette_size == 16:
#             for byte in image:
#                 top_nibble = (byte & 0xF0) >> 4
#                 bottom_nibble = byte & 0x0F

#                 result_image += palette[bottom_nibble] + palette[top_nibble]
#         else:
#             for byte in image:
#                 result_image += palette[byte]

#         return result_image
    

#     def render_image(self) -> Image.Image:
#         decomp_image = self.decompressed_image()
#         side_len = int(sqrt(len(decomp_image) >> 2))
#         return Image.frombytes('RGBA', (side_len, side_len), decomp_image)