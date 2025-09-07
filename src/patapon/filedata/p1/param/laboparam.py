from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from .generic import GenericParamHeader



@dataclass
class LaboParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("labo_param_count", "source"))


@dataclass
class LaboParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 1, count=24)})


@dataclass
class LaboParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[LaboParamInfoElement] = field(default_factory=list[LaboParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("labo_param_count", "count", 0)]})



@dataclass
class LaboParam(PataponDynamicDataClass):
    header: LaboParamHeader = field(default_factory=LaboParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    labo_params: LaboParamInfo = field(default_factory=LaboParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
