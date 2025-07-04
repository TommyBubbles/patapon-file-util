from dataclasses import field, dataclass
from .patapon_data_class import (
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
class GXSectionHeader(PataponStaticDataClass, PataponDataClassHeader):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("used_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("total_size", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})


@dataclass
class GXSectionBody(PataponDynamicDataClass, PataponDataClassBody):
    fl1: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 0), "tags": [FieldTag("used_size", "byte_count")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 1), "tags": [FieldTag("unk1_padding", "size", func=difference, func_params={"first": "total_size", "second": "used_size"})]})


@dataclass
class GXXFileHeader(PataponStaticDataClass):
    """
    Main Header for GXX Files
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
    animation_clips_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    unk2_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    unk2_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    unk1_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    unk1_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})


# Section 1 (Unknown 1)
@dataclass
class GXXUnknown1Header(PataponStaticDataClass, PataponDataClassHeader):
    pass


@dataclass
class GXXUnknown1Body(PataponStaticDataClass, PataponDataClassBody):
    pass


# Section 2 (Unknown 2)
class GXXUnknown2Header(GXSectionHeader):
    pass


class GXXUnknown2Body(GXSectionBody):
    pass


# Section 3 (Animation Clips)
class GXXAnimationClipElementHeader(GXSectionHeader):
    pass


class GXXAnimationClipElementBody(GXSectionBody):
    pass


@dataclass
class GXXAnimationClipElement(PataponDynamicDataClass, PataponDataClassHeader):
    header: GXXAnimationClipElementHeader = field(default_factory=GXXAnimationClipElementHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40), "tags": [FieldTag("anim_clip_element", "header")]})
    body: GXXAnimationClipElementBody = field(default_factory=GXXAnimationClipElementBody, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("anim_clip_element", "body")]})


@dataclass
class GXXAnimationClipSection(PataponDynamicDataClass):
    clips: list[GXXAnimationClipElement] = field(default_factory=list[GXXAnimationClipElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("anim_clip_size", "byte_size")]})





# Section 4 (Animation Information)
@dataclass
class GXXAnimationInfoHeader(PataponStaticDataClass, PataponDataClassHeader):
    num_element: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    file_footer_pointers_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    file_footer_pointers_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("gxx_footer_pointer_count", "source")]})
    anim_clip_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    anim_clip_info_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": FieldTag("anim_info_count", "source")})
    node_name_list_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    node_name_list_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("node_name_count", "source")]})
    fl1: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 8, count=6)})


# Section 4.1 (File Footer)
@dataclass
class GXXFileFooterPointers(PataponDynamicDataClass, PataponDataClassHeader):
    pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("gxx_footer_pointer_count", "count"), FieldTag("gxx_footer_pointer_list", "source")]})


# Section 4.2 (Animation Render Information)
@dataclass
class GXXAnimationInfoElement(PataponStaticDataClass):
    anim_clip_pointer_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    anim_frames: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    anim_framerate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    anim_loops: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})


@dataclass
class GXXAnimationInfoTable(PataponDynamicDataClass, PataponDataClassBody):
    anim_infos: list[GXXAnimationInfoElement] = field(default_factory=list[GXXAnimationInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("anim_info_count", "count")]})
    anim_pointer_num: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("anim_clip_count", "source")]})
    anim_clip_pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("anim_clip_count", "count")]})


# Section 4.3 (Node Name Information)
@dataclass
class GXXNodeNameElement(PataponStaticDataClass, PataponDataClassElement):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    name_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class GXXNodeNameListHeader(PataponDynamicDataClass, PataponDataClassHeader):
    node_info_list: list[GXXNodeNameElement] = field(default_factory=list[GXXNodeNameElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("node_name_count", "count"), FieldTag("node_name_sizes", "source")]})


@dataclass
class GXXNodeNameListBody(PataponDynamicDataClass, PataponDataClassBody):
    name_list: list[str] = field(default_factory=list[str], metadata={"meta": FieldMetadata("string", 0, encoding="utf-8"), "tags": [FieldTag("node_name_strings", "size", func=string_size_list, func_params={"list": "node_name_sizes", "end": "gxx_footer_pointer_list"})]})


# Section 4.1 (File Footer) (Cont.)
@dataclass
class GXXFileFooter(PataponDataClassBody, PataponStaticDataClass):
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
class GXXAnimationInfoSection(PataponDynamicDataClass, PataponDataClassBody):
    info_header: GXXAnimationInfoHeader = field(default_factory=GXXAnimationInfoHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file_footer_header", "header"), FieldTag("anim_info_table", "header"), FieldTag("node_name_header", "header")]})
    footer_pointer_info: GXXFileFooterPointers = field(default_factory=GXXFileFooterPointers, metadata={"meta": FieldMetadata("header", 1), "tags": [FieldTag("file_footer_header", "body")]})
    anim_info_table: GXXAnimationInfoTable = field(default_factory=GXXAnimationInfoTable, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("anim_info_table", "body")]})
    node_name_list_header: GXXNodeNameListHeader = field(default_factory=GXXNodeNameListHeader, metadata={"meta": FieldMetadata("header", 3), "tags": [FieldTag("node_name_header", "body"), FieldTag("node_name", "header")]})
    node_name_list_body: GXXNodeNameListBody = field(default_factory=GXXNodeNameListBody, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("node_name", "body")]})
    file_footer: GXXFileFooter = field(default_factory=GXXFileFooter, metadata={"meta": FieldMetadata("body", 5)})


# Base GXX class
@dataclass
class GXX(PataponDynamicDataClass):
    file_header: GXXFileHeader = field(default_factory=GXXFileHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("anim_clip", "header")]})
    unk1_header: GXXUnknown1Header = field(default_factory=GXXUnknown1Header, metadata={"meta": FieldMetadata("header", 1), "tags": [FieldTag("unk1", "header")]})
    unk1_body: GXXUnknown1Body = field(default_factory=GXXUnknown1Body, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("unk1", "body")]})
    unk2_header: GXXUnknown2Header = field(default_factory=GXXUnknown2Header, metadata={"meta": FieldMetadata("header", 3), "tags": [FieldTag("unk2", "header")]})
    unk2_body: GXXUnknown2Body = field(default_factory=GXXUnknown2Body, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("unk2", "body")]})
    anim_clip_section: GXXAnimationClipSection = field(default_factory=GXXAnimationClipSection, metadata={"meta": FieldMetadata("body", 5), "tags": [FieldTag("anim_clip", "body")]})
    anim_info_section: GXXAnimationInfoSection = field(default_factory=GXXAnimationInfoSection, metadata={"meta": FieldMetadata("body", 6)})