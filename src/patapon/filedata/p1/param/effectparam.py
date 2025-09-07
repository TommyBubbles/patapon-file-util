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
class EffectParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("effect_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("effect_damage_param_count", "source"))



@dataclass
class EffectParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    hitEffectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    categoryId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    damageParamName: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    renderPriority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    alphaBlendType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    isAimMovingDirection: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    isGroundHitWhenDestroy: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    isHitWhenDestroy: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    isGroundHitWhenCallback: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    isCollision: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    isPhysics: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    mass: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 13)})
    boundCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    attenuationX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 15)})
    attenuationY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 16)})
    windDrag: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 17)})
    timeScale: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    collisionX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    collisionY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 20)})
    collisionRadius: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 21)})
    userId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 22)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 23, size=0x20)})
    shotLabelId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 24)})
    hitLabelId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 25)})


@dataclass
class EffectParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[EffectParamInfoElement] = field(default_factory=list[EffectParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("effect_param_count", "count", 0)]})



@dataclass
class EffectDamageParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 1)})


@dataclass
class EffectDamageParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[EffectDamageParamElement] = field(default_factory=list[EffectDamageParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("effect_damage_param_count", "count", 1)]})



@dataclass
class EffectParam(PataponDynamicDataClass):
    header: EffectParamHeader = field(default_factory=EffectParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    effect_params: EffectParamInfo = field(default_factory=EffectParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    effect_damage_params: EffectDamageParam = field(default_factory=EffectDamageParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    