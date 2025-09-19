from PIL import Image
from math import sqrt

from dataclasses import field, dataclass
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponDataClassElement,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    FieldMetadata,
    FieldTag
)


@dataclass
class GXTHeader(PataponDataClassHeader, PataponStaticDataClass):
    magic: bytes = field(default=b"XXG.01.0MIG.", metadata={"meta": FieldMetadata("bytes", 0, size=0x10)})
    offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    texture_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    texture_info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    motion_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    motion_info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    unknown_1_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    unknown_1_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    image_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    image_infosize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})



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



def difference(first: int, second: int) -> int:
    return first - second


@dataclass
class MotionInfoHeader(PataponDataClassHeader, PataponStaticDataClass):
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("motion_info_used_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("motion_info_total_size", "source")]})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})



@dataclass
class GxMotionCommand(PataponStaticDataClass, PataponDataClassElement):
    value: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 0, size=3)})
    command_id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 1)})


@dataclass
class MotionInfoBody(PataponDataClassBody, PataponDynamicDataClass):
    fl1: list[GxMotionCommand] = field(default_factory=list[GxMotionCommand], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("motion_info_used_size", "byte_size")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 1), "tags": [FieldTag("fl1_padding", "size", func=difference, func_params={"first": "motion_info_total_size", "second": "motion_info_used_size"})]})



@dataclass
class TextureInfo(PataponDataClassBody, PataponStaticDataClass):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    file_name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=2)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    width: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    height: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    i6: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    i7: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    motion_command_offset_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    count_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 11)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 12, count=2)})
    count_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 13)})
    motion_command_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 14)})
    file_name: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20, encoding="utf-8")})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 16, count=6)})



@dataclass
class GXT(PataponDynamicDataClass):
    file_header: GXTHeader = field(default_factory=GXTHeader, metadata={"meta": FieldMetadata("dataclass", 0)})
    image_header: GXTImageHeader = field(default_factory=GXTImageHeader, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("image", "header")]})
    image_body: GXTImageBody = field(default_factory=GXTImageBody, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("image", "body")]})
    palette_header: GXTPaletteHeader = field(default_factory=GXTPaletteHeader, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("palette", "header")]})
    palette_body: GXTPaletteBody = field(default_factory=GXTPaletteBody, metadata={"meta": FieldMetadata("dataclass", 4), "tags": [FieldTag("palette", "body")]})
    unknown_1_header: GXTUnknown1Header = field(default_factory=GXTUnknown1Header, metadata={"meta": FieldMetadata("dataclass", 5), "tags": [FieldTag("unknown_1", "header")]})
    unknown_1_body: GXTUnknown1Body = field(default_factory=GXTUnknown1Body, metadata={"meta": FieldMetadata("dataclass", 6), "tags": [FieldTag("unknown_1", "body")]})
    motion_info_header: MotionInfoHeader = field(default_factory=MotionInfoHeader, metadata={"meta": FieldMetadata("dataclass", 7), "tags": [FieldTag("motion_info", "header")]})
    motion_info_body: MotionInfoBody = field(default_factory=MotionInfoBody, metadata={"meta": FieldMetadata("dataclass", 8), "tags": [FieldTag("motion_info", "body")]})
    texture_info: TextureInfo = field(default_factory=TextureInfo, metadata={"meta": FieldMetadata("dataclass", 9)})

    def decompressed_image(self) -> bytes:
        image: bytes = self.image_body.raw_image
        palette: list[bytes] = self.palette_body.palette
        palette_size: int = len(palette)
        
        result_image: bytes = b''
        if palette_size == 16:
            for byte in image:
                top_nibble = (byte & 0xF0) >> 4
                bottom_nibble = byte & 0x0F

                result_image += palette[bottom_nibble] + palette[top_nibble]
        else:
            for byte in image:
                result_image += palette[byte]

        return result_image
    

    def render_image(self) -> Image.Image:
        decomp_image = self.decompressed_image()
        return Image.frombytes('RGBA', (self.texture_info.width, self.texture_info.height), decomp_image)