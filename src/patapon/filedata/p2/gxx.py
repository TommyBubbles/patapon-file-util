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
from .func.field_func import difference, string_size_list


@dataclass
class GxSectionHeader(PataponStaticDataClass, PataponDataClassHeader):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("used_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("total_size", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})


@dataclass
class GxSectionBody(PataponDynamicDataClass, PataponDataClassBody):
    fl1: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 0), "tags": [FieldTag("used_size", "byte_count")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 1), "tags": [FieldTag("unk1_padding", "size", func=difference, func_params={"first": "total_size", "second": "used_size"})]})


@dataclass
class GxxFileHeader(PataponStaticDataClass):
    """
    Main Header for Gxx Files
    Basic Breakdown:
        - starts with magic to determine the type of file it is
        - TBD (seems to suggest an offset of some kind)
        - pointers to and sizes of four different sections of information listed
          in reverse order than they are stored physically on the file
            1. Animation Information
            2. Animation Clip Information
            3. Unknown (similiar storage style to animation clip information)
            4. Unknown (empty space?)
    """
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x10, encoding="utf-8")})
    file_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    footer_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    footer_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    animation_clips_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    animation_clips_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6), "tags": [FieldTag("anim_clip_size", "source")]})
    unk2_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    unk2_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    unk1_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    unk1_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})


# Section 1 (Unknown 1)
@dataclass
class GxxUnknown1Header(PataponStaticDataClass, PataponDataClassHeader):
    pass


@dataclass
class GxxUnknown1Body(PataponStaticDataClass, PataponDataClassBody):
    pass


# Section 2 (Unknown 2)
class GxxUnknown2Header(GxSectionHeader):
    pass


class GxxUnknown2Body(GxSectionBody):
    pass


# Section 3 (Animation Clips)
class GxxAnimationClipElementHeader(GxSectionHeader):
    pass


class GxxAnimationClipElementBody(GxSectionBody):
    pass


@dataclass
class GxxAnimationClipElement(PataponDynamicDataClass, PataponDataClassHeader):
    header: GxxAnimationClipElementHeader = field(default_factory=GxxAnimationClipElementHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40), "tags": [FieldTag("anim_clip_element", "header")]})
    body: GxxAnimationClipElementBody = field(default_factory=GxxAnimationClipElementBody, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("anim_clip_element", "body")]})


@dataclass
class GxxAnimationClipSection(PataponDynamicDataClass):
    clips: list[GxxAnimationClipElement] = field(default_factory=list[GxxAnimationClipElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("anim_clip_size", "byte_size")]})


# Section 4 (Animation Information)
@dataclass
class GxxAnimationInfoHeader(PataponStaticDataClass, PataponDataClassHeader):
    num_element: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    file_footer_pointers_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    file_footer_pointers_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("Gxx_footer_pointer_count", "source")]})
    anim_clip_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    anim_clip_info_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": FieldTag("anim_info_count", "source")})
    node_name_list_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    node_name_list_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("node_name_count", "source")]})
    fl1: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 8, count=6)})


# Section 4.1 (File Footer)
@dataclass
class GxxFileFooterPointers(PataponDynamicDataClass, PataponDataClassHeader):
    pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("Gxx_footer_pointer_count", "count"), FieldTag("Gxx_footer_pointer_list", "source")]})


# Section 4.2 (Animation Render Information)
@dataclass
class GxxAnimationInfoElement(PataponStaticDataClass):
    anim_clip_pointer_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    anim_frames: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    anim_framerate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    anim_loops: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})


@dataclass
class GxxAnimationInfoTable(PataponDynamicDataClass, PataponDataClassBody):
    anim_infos: list[GxxAnimationInfoElement] = field(default_factory=list[GxxAnimationInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("anim_info_count", "count")]})
    anim_pointer_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("anim_clip_count", "source")]})
    anim_clip_pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("anim_clip_count", "count")]})


# Section 4.3 (Node Name Information)
@dataclass
class GxxNodeNameElement(PataponStaticDataClass, PataponDataClassElement):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    name_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class GxxNodeNameListHeader(PataponDynamicDataClass, PataponDataClassHeader):
    node_info_list: list[GxxNodeNameElement] = field(default_factory=list[GxxNodeNameElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("node_name_count", "count"), FieldTag("node_name_sizes", "source")]})


@dataclass
class GxxNodeNameListBody(PataponDynamicDataClass, PataponDataClassBody):
    name_list: list[str] = field(default_factory=list[str], metadata={"meta": FieldMetadata("string", 0, encoding="utf-8"), "tags": [FieldTag("node_name_strings", "size", func=string_size_list, func_params={"list": "node_name_sizes", "end": "Gxx_footer_pointer_list"})]})


# Section 4.1 (File Footer) (Cont.)
@dataclass
class GxxFileFooter(PataponDataClassBody, PataponStaticDataClass):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    file_name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=2)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    i4: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    i5: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=2)})
    i6: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    i7: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    file_name: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x10, encoding="utf-8")})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 12, count=2)})


@dataclass
class GxxAnimationInfoSection(PataponDynamicDataClass, PataponDataClassBody):
    info_header: GxxAnimationInfoHeader = field(default_factory=GxxAnimationInfoHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x38), "tags": [FieldTag("file_footer_header", "header"), FieldTag("anim_info_table", "header"), FieldTag("node_name_header", "header")]})
    footer_pointer_info: GxxFileFooterPointers = field(default_factory=GxxFileFooterPointers, metadata={"meta": FieldMetadata("header", 1), "tags": [FieldTag("file_footer_header", "body")]})
    anim_info_table: GxxAnimationInfoTable = field(default_factory=GxxAnimationInfoTable, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("anim_info_table", "body")]})
    node_name_list_header: GxxNodeNameListHeader = field(default_factory=GxxNodeNameListHeader, metadata={"meta": FieldMetadata("header", 3), "tags": [FieldTag("node_name_header", "body"), FieldTag("node_name", "header")]})
    node_name_list_body: GxxNodeNameListBody = field(default_factory=GxxNodeNameListBody, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("node_name", "body")]})
    file_footer: GxxFileFooter = field(default_factory=GxxFileFooter, metadata={"meta": FieldMetadata("body", 5)})


# Base Gxx class
@dataclass
class Gxx(PataponDynamicDataClass):
    file_header: GxxFileHeader = field(default_factory=GxxFileHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("anim_clip", "header")]})
    unk1_header: GxxUnknown1Header = field(default_factory=GxxUnknown1Header, metadata={"meta": FieldMetadata("header", 1), "tags": [FieldTag("unk1", "header")]})
    unk1_body: GxxUnknown1Body = field(default_factory=GxxUnknown1Body, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("unk1", "body")]})
    unk2_header: GxxUnknown2Header = field(default_factory=GxxUnknown2Header, metadata={"meta": FieldMetadata("header", 3), "tags": [FieldTag("unk2", "header")]})
    unk2_body: GxxUnknown2Body = field(default_factory=GxxUnknown2Body, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("unk2", "body")]})
    anim_clip_section: GxxAnimationClipSection = field(default_factory=GxxAnimationClipSection, metadata={"meta": FieldMetadata("body", 5), "tags": [FieldTag("anim_clip", "body")]})
    anim_info_section: GxxAnimationInfoSection = field(default_factory=GxxAnimationInfoSection, metadata={"meta": FieldMetadata("body", 6)})