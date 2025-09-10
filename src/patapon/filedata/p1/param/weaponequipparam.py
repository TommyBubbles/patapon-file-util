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
class WeaponParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("equip_param_count", "source", 0, sub_tag))



# used for equipparam.dat files from equip folder on a per equipment basis
@dataclass
class EquipParam(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    itemId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    categoryId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    useCharaId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    troopId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    shotEffectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=7)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 9)})
    modelFileName: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    effectModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})


@dataclass
class EquipParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[EquipParam] = field(default_factory=list[EquipParam], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("equip_param_count", "count")]})



@dataclass
class WeaponParam(PataponDynamicDataClass):
    header: WeaponParamHeader = field(default_factory=WeaponParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    equip_params: EquipParamInfo = field(default_factory=EquipParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})