from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from .generic import GenericParamHeader



@dataclass
class MotionTimingParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("mtiming_base_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("mtiming_name_list_param_count", "source", 1, sub_tag))



@dataclass
class BaseParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    isUse: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=2)})
    mtpCategoryId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 5, count=3)})
    tcp_checkType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    nodeNameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    motionId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    type: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    timing: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 11, count=3)})
    ep_checkType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    appearNodeNameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    eventId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    filler_4: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 16)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 17)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    f2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 20, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 21, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 22, size=0x20)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 23, size=0x20)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("mtiming_base_param_count", "count")]})



@dataclass
class NameListParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    rsv3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=7)})
    nameStr: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x40)})


@dataclass
class NameListParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[NameListParamElement] = field(default_factory=list[NameListParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("mtiming_name_list_param_count", "count")]})



@dataclass
class MotionTimingParam(PataponDynamicDataClass):
    header: MotionTimingParamHeader = field(default_factory=MotionTimingParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    name_list_params: NameListParam = field(default_factory=NameListParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})