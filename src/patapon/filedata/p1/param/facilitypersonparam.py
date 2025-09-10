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
class ParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("fp_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("fp_model_param_count", "source", 1, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("fp_attach_param_count", "source", 2, sub_tag))


@dataclass
class AuxesisParam(PataponStaticDataClass, PataponDataClassElement):
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    pri: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    seedCost: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    personalCost: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})


@dataclass
class ParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    poolSize: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    scriptName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    auxesisParam: list[AuxesisParam] = field(default_factory=list[AuxesisParam], metadata={"meta": FieldMetadata("element_list", 4, count=3)})
    type: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    pad: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 6, count=2)})


@dataclass
class ParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ParamElement] = field(default_factory=list[ParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("fp_param_count", "count")]})



@dataclass
class MotionParam(PataponStaticDataClass, PataponDataClassElement):
    startFrame: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
    nFrame: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})


@dataclass
class ModelParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 1, size=0x20)})
    buildName: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x20)})
    wreckName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    resourceType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 4)})
    nAttach: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 5)})
    attachName: list[str] = field(default_factory=list[str], metadata={"meta": FieldMetadata("string", 6, count=5, size=0x20)})
    width: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    nBuildMotionParam: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 8)})
    nWreckMotionParam: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 9)})
    motionParam: list[MotionParam] = field(default_factory=list[MotionParam], metadata={"meta": FieldMetadata("element_list", 10, count=9)})


@dataclass
class ModelParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ModelParamElement] = field(default_factory=list[ModelParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("fp_model_param_count", "count")]})



@dataclass
class AttachParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    nAttach: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    modelAttachNodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x20)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    particleAttachNodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    particleId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    isEnableSearch: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})


@dataclass
class AttachParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[AttachParamElement] = field(default_factory=list[AttachParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("fp_attach_param_count", "count")]})



@dataclass
class FacilityPersonParam(PataponDynamicDataClass):
    header: ParamHeader = field(default_factory=ParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    params: ParamInfo = field(default_factory=ParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    model_params: ModelParam = field(default_factory=ModelParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    attach_params: AttachParam = field(default_factory=AttachParam, metadata={"meta": FieldMetadata("body", 3), "tags": [FieldTag("file", "body")]})
