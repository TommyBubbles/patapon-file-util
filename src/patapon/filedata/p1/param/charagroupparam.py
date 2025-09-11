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
class CharaGroupParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("chara_group_param_count", "source", 0, sub_tag))



@dataclass
class CharaGroupParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    rsv2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=6)})
    charaFlag: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 4, count=16)})


@dataclass
class CharaGroupParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CharaGroupParamInfoElement] = field(default_factory=list[CharaGroupParamInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("chara_group_param_count", "count")]})



@dataclass
class CharaGroupParam(PataponDynamicDataClass):
    header: CharaGroupParamHeader = field(default_factory=CharaGroupParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    chara_group_params: CharaGroupParamInfo = field(default_factory=CharaGroupParamInfo, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})