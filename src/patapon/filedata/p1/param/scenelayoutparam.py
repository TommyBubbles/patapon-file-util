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
class SceneLayoutParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("sl_layout_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("sl_animation_param_count", "source", 1, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("sl_texture_rectangle_param_count", "source", 2, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("sl_unknown_param_count", "source", 3, sub_tag))



@dataclass
class LayoutParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    offsetX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    offsetY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    rectX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    rectY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    rectW: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    rectH: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 8)})
    colorR: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    colorG: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    colorB: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    colorA: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    texRectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    priority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    isUse: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    isCenterPos: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 16)})
    animId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 17)})
    isPlayAnim: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 18)})
    isSizeIsTexSize: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 19)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 20, count=5)})


@dataclass
class LayoutParam(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[LayoutParamElement] = field(default_factory=list[LayoutParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sl_layout_param_count", "count")]})



@dataclass
class AnimationParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    animType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    posX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    posY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    sizeW: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    sizeH: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    deg: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    alpha: float = field(default=0, metadata={"meta": FieldMetadata("float", 8)})
    texAnimX: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    texAnimY: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    texAnimType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    animSec: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 12)})
    nextId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    isUseReturn: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    progressRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 15)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 16)})
    initVecX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 17)})
    initVecY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    initRad_1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 20)})
    initRad_2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 21)})
    gravity: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 22)})
    hitFlag: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 23)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 24)})


@dataclass
class AnimationParam(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[AnimationParamElement] = field(default_factory=list[AnimationParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sl_animation_param_count", "count")]})



@dataclass
class TextureRectanleParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    texId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    rectX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    rectY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    rectW: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    rectH: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 8)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 9, count=16)})


@dataclass
class TextureRectanleParam(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[TextureRectanleParamElement] = field(default_factory=list[TextureRectanleParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sl_texture_rectangle_param_count", "count")]})



@dataclass
class Unknown1ParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=23)})


@dataclass
class Unknown1Param(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[Unknown1ParamElement] = field(default_factory=list[Unknown1ParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sl_unknown_param_count", "count")]})



@dataclass
class Unknown2ParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=23)})


@dataclass
class Unknown2Param(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[Unknown2ParamElement] = field(default_factory=list[Unknown2ParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sl_unknown_param_count", "count")]})



@dataclass
class SceneLayoutParam(PataponDynamicDataClass):
    header: SceneLayoutParamHeader = field(default_factory=SceneLayoutParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    layout_params: LayoutParam = field(default_factory=LayoutParam, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    animation_params: AnimationParam = field(default_factory=AnimationParam, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
    texture_rectangle_params: TextureRectanleParam = field(default_factory=TextureRectanleParam, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("file", "body")]})
    unknown_1_params: Unknown1Param = field(default_factory=Unknown1Param, metadata={"meta": FieldMetadata("dataclass", 4), "tags": [FieldTag("file", "body")]})
    unknown_2_params: Unknown2Param = field(default_factory=Unknown2Param, metadata={"meta": FieldMetadata("dataclass", 5), "tags": [FieldTag("file", "body")]})