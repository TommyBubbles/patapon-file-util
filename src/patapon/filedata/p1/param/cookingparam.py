from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from . import DamageParam
from .generic import GenericParamHeader



@dataclass
class CookingParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("cooking_param_count", "source", 0, sub_tag))



@dataclass
class CookingParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    itemId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 3)})


@dataclass
class CookingParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CookingParamInfoElement] = field(default_factory=list[CookingParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("cooking_param_count", "count")]})



@dataclass
class CookingParam(PataponDynamicDataClass):
    header: CookingParamHeader = field(default_factory=CookingParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    chara_group_params: CookingParamInfo = field(default_factory=CookingParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})