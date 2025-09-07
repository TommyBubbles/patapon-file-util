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
class UnitParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("base_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("troop_type_param_count", "source"))



@dataclass
class BaseParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=7)})
    squadAddCheckLength: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    unitDecay: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    unitDecay_floating: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    knockBackPower: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    unitDecay_slip: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    slipRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 8)})
    knockBackBrake: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 9)})
    defPtclFrame: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    escapeJumpTimingRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    escapeJumpPower_X: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 12)})
    escapeJumpPower_Y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 13)})
    escapeJumpVecRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 14)})
    moveSpeedRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 15)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 16, count=3)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("base_param_count", "count", 0)]})



@dataclass
class TroopTypeParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=7)})
    dmy_squadAddCheckLength: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    dmy_unitDecay: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    dmy_unitDecay_floating: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    dmy_knockBackPower: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    moveLineStyle_Range: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    moveLineStyle_PowerRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 8)})
    moveLineStyle_ratioClampMin: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 9)})
    squadTargetTauchRange: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 11, count=8)})


@dataclass
class TroopTypeParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[TroopTypeParamElement] = field(default_factory=list[TroopTypeParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("troop_type_param_count", "count", 1)]})



@dataclass
class UnitParam(PataponDynamicDataClass):
    header: UnitParamHeader = field(default_factory=UnitParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    troop_type_params: TroopTypeParam = field(default_factory=TroopTypeParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
