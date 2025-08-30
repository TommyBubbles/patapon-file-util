from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)


@dataclass
class StageAreaParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    id: str = field(default="LAST", metadata={"meta": FieldMetadata("string", 0, size=0x4)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
    offsetStage: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    offsetAreaParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    offsetArea: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    offsetPoint: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    offsetEventBox: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    offsetEnemySquad: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    offsetGimmick: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})



@dataclass
class StageParam(PataponStaticDataClass, PataponDataClassBody):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})



@dataclass
class AreaParamParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    modelName_1: str = field(default="", metadata={"meta": FieldMetadata("string", 1, size=0x20)})
    modelName_2: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x20)})
    modelName_3: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    modelName_4: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    ceilingModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x20)})
    ModelName_1: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    shinySkyModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    rainySkyModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    shinyGradationModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    rainyGradationModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    shinyTopColor: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 11, count=4)})
    shinyBottomColor: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 12, count=4)})
    rainyTopColor: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 13, count=4)})
    rainyBottomColor: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 14, count=4)})


@dataclass
class AreaParamParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("area_param_param_count", "source")]})
    areaParamParamList: list[AreaParamParamElement] = field(default_factory=list[AreaParamParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("area_param_param_count", "count")]})



@dataclass
class AreaParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    paramId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class AreaParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("area_param_count", "source")]})
    areaParamList: list[AreaParamElement] = field(default_factory=list[AreaParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("area_param_count", "count")]})



@dataclass
class PointParamElement():
    x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
    y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})


@dataclass
class PointParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("point_param_count", "source")]})
    areaParamList: list[AreaParamElement] = field(default_factory=list[AreaParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("point_param_count", "count")]})



@dataclass
class EventBoxParamElement(PataponStaticDataClass, PataponDataClassElement):
    x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
    y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
    width: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    height: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    riseType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    targetType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    targetCategory: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    target: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    isUseStartFlag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    isUseEndFlag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    isAllwaysActive: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})


@dataclass
class EventBoxParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("event_box_param_count", "source")]})
    eventBoxParamList: list[EventBoxParamElement] = field(default_factory=list[EventBoxParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("event_box_param_count", "count")]})



@dataclass
class SquadParamElement(PataponStaticDataClass, PataponDataClassElement):
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
    y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    width: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    height: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    renderPriority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    unitName: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x40)})
    unitNum: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    unitLevel: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    weaponLevel: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    isFixed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    isAutoAppearance: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    isForceStay: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    weaponName: str = field(default="", metadata={"meta": FieldMetadata("string", 12, size=0x40)})
    equipName1: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x40)})
    equipName2: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x40)})


@dataclass
class SquadParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("squad_param_count", "source")]})
    squadParamList: list[SquadParamElement] = field(default_factory=list[SquadParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("squad_param_count", "count")]})



@dataclass
class GimmickLayoutParamElement(PataponStaticDataClass, PataponDataClassElement):
    paramName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
    y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    renderPriority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    riseType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    targetType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    targetCategory: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    target: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    isUseStartFlag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    isUseEndFlag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    isAllwaysActive: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})


@dataclass
class GimmickLayoutParam(PataponDynamicDataClass, PataponDataClassBody):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("gimmick_layout_param_count", "source")]})
    gimmickLayoutParamList: list[GimmickLayoutParamElement] = field(default_factory=list[GimmickLayoutParamElement], metadata={"meta": FieldMetadata("element", 1), "tags": [FieldTag("gimmick_layout_param_count", "count")]})



@dataclass
class StageAreaParam(PataponDynamicDataClass):
    header: StageAreaParamHeader = field(default_factory=StageAreaParamHeader, metadata={"meta": FieldMetadata("header", 0)})
    stageParam: StageParam = field(default_factory=StageParam, metadata={"meta": FieldMetadata("body", 1)})
    areaParamParam: AreaParamParam = field(default_factory=AreaParamParam, metadata={"meta": FieldMetadata("body", 2)})
    areaParam: AreaParam = field(default_factory=AreaParam, metadata={"meta": FieldMetadata("body", 3)})
    pointParam: PointParam = field(default_factory=PointParam, metadata={"meta": FieldMetadata("body", 4)})
    eventBoxParam: EventBoxParam = field(default_factory=EventBoxParam, metadata={"meta": FieldMetadata("body", 5)})
    squadParam: SquadParam = field(default_factory=SquadParam, metadata={"meta": FieldMetadata("body", 6)})
    gimmickLayoutParam: GimmickLayoutParam = field(default_factory=GimmickLayoutParam, metadata={"meta": FieldMetadata("body", 7)})