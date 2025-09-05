from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag
from patapon.filedata.p1.param import DamageParam


@dataclass
class CharaBirthParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    birth_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("birth_param_count", "source")]})
    birth_param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    adjust_damage_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("adjust_damage_param_count", "source")]})
    adjust_damage_param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 9, count=4)})



@dataclass
class BirthParamElement(PataponStaticDataClass, PataponDataClassElement):
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    subspeciesNameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 1)})
    unitNameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 2)})
    unitName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    adjustDamageParamName: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    rgba: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int8", 5, count=4)})
    defaultEquipItemId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 6, count=3)})
    defaultEquipState: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 7, count=3)})
    itemId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=2)})
    cost: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    padding: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 10, count=4)})


@dataclass
class BirthParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BirthParamElement] = field(default_factory=list[BirthParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("birth_param_count", "count")]})



@dataclass
class AdjustDamageParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 1)})


@dataclass
class AdjustDamageParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[AdjustDamageParamElement] = field(default_factory=list[AdjustDamageParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("adjust_damage_param_count", "count")]})



@dataclass
class CharaBirthParam(PataponDynamicDataClass):
    header: CharaBirthParamHeader = field(default_factory=CharaBirthParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    birth_params: BirthParam = field(default_factory=BirthParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    adjust_damage_params: AdjustDamageParam = field(default_factory=AdjustDamageParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})