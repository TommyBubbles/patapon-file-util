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
class SystemParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("s_unknown_1_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("s_unknown_2_param_count", "source", 1, sub_tag))



@dataclass
class Unknown1ParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})


@dataclass
class Unknown1Param(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[Unknown1ParamElement] = field(default_factory=list[Unknown1ParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("s_unknown_1_param_count", "count")]})



@dataclass
class Unknown2ParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})


@dataclass
class Unknown2Param(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[Unknown2ParamElement] = field(default_factory=list[Unknown2ParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("s_unknown_2_param_count", "count")]})



@dataclass
class SystemParam(PataponDynamicDataClass):
    header: SystemParamHeader = field(default_factory=SystemParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    unknown_1_params: Unknown1Param = field(default_factory=Unknown1Param, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    unknown_2_params: Unknown2Param = field(default_factory=Unknown2Param, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
