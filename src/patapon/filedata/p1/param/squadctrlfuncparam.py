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
class SquadCtrlFuncParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("scf_base_param_count", "source", 0, sub_tag))



@dataclass
class BaseParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    scriptId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=6)})
    targetType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    targetRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    rangeRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    enableRangeRatio: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    offsetX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 8)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 9, count=3)})
    attackArea: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    priorityCharaType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    modelDirType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    forceMove: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    forceAttack: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    callParticleId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 15, count=3)})
    changeMotionId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 16, count=16)})
    isTargetTouch: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 17)})
    sec: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    touchEndSec: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    attackCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 20)})
    damageCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 21)})
    scriptLabelId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 22)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 23, count=2)})
    nextState: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 24)})
    isCounterClear: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 25)})
    isAutoCtrlClear: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 26)})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 27, count=5)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("scf_base_param_count", "count")]})



@dataclass
class SquadCtrlFuncParam(PataponDynamicDataClass):
    header: SquadCtrlFuncParamHeader = field(default_factory=SquadCtrlFuncParamHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
