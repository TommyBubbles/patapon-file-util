from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from . import DamageParam
from .generic import GenericParamHeader


@dataclass
class SquadActivityParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("sa_base_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("sa_missile_param_count", "source", 1, sub_tag))



@dataclass
class BaseParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    scriptId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    enableCharaType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    filler_1: list[int]  = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=5)})
    ctrlFuncParamId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    attackRange: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    attackMoveRange: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    missileId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    rangeRatioAP: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 9)})
    rangeBackEnd: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    effectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    isBrake: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 12)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x20)})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 17, size=0x20)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("dataclass", 18)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sa_base_param_count", "count")]})



@dataclass
class MissileParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    initSpeed: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    initSpeedRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    degree: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    degreeRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    windRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=3)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})


@dataclass
class MissileParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[MissileParamElement] = field(default_factory=list[MissileParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sa_missile_param_count", "count")]})



@dataclass
class SquadActivityParam(PataponDynamicDataClass):
    header: SquadActivityParamHeader = field(default_factory=SquadActivityParamHeader, metadata={"meta": FieldMetadata("dataclass", 0, data_size=0x40), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    missile_params: MissileParam = field(default_factory=MissileParam, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
