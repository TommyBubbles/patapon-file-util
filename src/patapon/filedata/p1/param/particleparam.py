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
class ParticleParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("particle_param_count", "source", 0, sub_tag))



@dataclass
class ParticleParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    particleId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    textureId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})


@dataclass
class ParticleParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ParticleParamInfoElement] = field(default_factory=list[ParticleParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("particle_param_count", "count")]})



@dataclass
class ParticleParam(PataponDynamicDataClass):
    header: ParticleParamHeader = field(default_factory=ParticleParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    particle_params: ParticleParamInfo = field(default_factory=ParticleParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
