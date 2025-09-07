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
from . import DamageParam


@dataclass
class StageAreaParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    id: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 0, size=0x4)})
    version: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    numGimmickParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("gimmick_param_count", "source")]})
    gimmickParamSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    gimmickParamAddr: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    numModelParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("model_param_count", "source")]})
    modelParamSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    modelParamAddr: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})



@dataclass
class GimmickParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    renderPriorityOffset_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    mainModelName_1: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    subModelName_1: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    renderPriorityOffset_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    mainModelName_2: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    subModelName_2: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    isCollision: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    isPush: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    isTall: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    collisionPosX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    collisionPosY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 12)})
    collisionSizeX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 13)})
    collisionSizeY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 14)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 15)})


@dataclass
class GimmickParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[GimmickParamElement] = field(default_factory=list[GimmickParamElement], metadata={"meta": FieldMetadata("element", 0), "tags": [FieldTag("gimmick_param_count", "count")]})



@dataclass
class ModelParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="GIMC", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    motionIDs: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 1, count=19)})


@dataclass
class ModelParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ModelParamElement] = field(default_factory=list[ModelParamElement], metadata={"meta": FieldMetadata("element", 0), "tags": [FieldTag("model_param_count", "count")]})



@dataclass
class StageGimmickParam(PataponDynamicDataClass):
    header: StageAreaParamHeader = field(default_factory=StageAreaParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    gimmickParam: GimmickParam = field(default_factory=GimmickParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    modelParam: ModelParam = field(default_factory=ModelParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})