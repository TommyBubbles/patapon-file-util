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
class MotionTypeParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("mtype_base_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("mtype_unknown_1_param_count", "source", 1, sub_tag))



@dataclass
class BaseParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=3)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 5, count=2)})
    priority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    isLoop: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    modelDirType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 9, count=5)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("mtype_base_param_count", "count")]})



@dataclass
class MotionTypeParam(PataponDynamicDataClass):
    header: MotionTypeParamHeader = field(default_factory=MotionTypeParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})