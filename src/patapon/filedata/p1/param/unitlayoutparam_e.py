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
class UnitLayoutParamEHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("troop_adding_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("squad_adding_param_count", "source", 1, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("ule_unknown_1_param_count", "source", 2, sub_tag))



# unsure on the validity of the field names because there are many other fields that where omitted
@dataclass
class TroopAddingParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    squadNum: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    posX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 4, count=5)})
    uap_aName: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x20)})
    uap_id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    uniqueId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    level: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    experience: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    weaponId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    weaponAttributeId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    isLive: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    deadCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})


@dataclass
class TroopAddingParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[TroopAddingParamElement] = field(default_factory=list[TroopAddingParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("troop_adding_param_count", "count")]})



# unsure on the validity of the field names because there are many other fields that where omitted
@dataclass
class SquadAddingParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    unitNum: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 2)})
    initUnitNum: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 3)})
    isFixed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 4)})
    isDefaultAppear: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 5)})
    charaId_dmy: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 6)})
    isUseDefaultUnitParam: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 7)})
    renderPriority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    isDefaultStay: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 10, count=6)})
    posX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    posY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 12)})
    posZ: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 13)})
    posRandX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 14)})
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20)})
    crc: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 16)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 17, count=3)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 18)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 19, count=3)})


@dataclass
class SquadAddingParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[SquadAddingParamElement] = field(default_factory=list[SquadAddingParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("squad_adding_param_count", "count")]})



@dataclass
class UnitLayoutParamE(PataponDynamicDataClass):
    header: UnitLayoutParamEHeader = field(default_factory=UnitLayoutParamEHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40), "tags": [FieldTag("file", "header")]})
    troop_adding_params: TroopAddingParam = field(default_factory=TroopAddingParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    squad_adding_params: SquadAddingParam = field(default_factory=SquadAddingParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
