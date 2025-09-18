from dataclasses import dataclass, field
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponDataClassElement,
    PataponDynamicDataClass,
    PataponStaticDataClass,
    FieldMetadata,
    FieldTag
)



@dataclass
class EffectKeyHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="EFFECT2", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    next: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    nKeyData: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 2), "tags": [FieldTag("key_data_count", "source")]})
    size_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 3)})



@dataclass
class RectangleUC(PataponStaticDataClass, PataponDataClassElement):
    w: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 0)})
    y: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 1)})
    x: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 2)})
    h: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 3)})


@dataclass
class EffectKeyData(PataponDynamicDataClass, PataponDataClassHeader):
    type: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 0)})
    flag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 1)})
    texno: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 2)})
    texw: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 3)})
    texh: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 4)})
    width: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 5)})
    height: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 6)})
    nParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 7), "tags": [FieldTag("particle_param_count", "source")]})
    st: list[RectangleUC] = field(default_factory=list[RectangleUC], metadata={"meta": FieldMetadata("dataclass", 8, count=16)})
    exFunc: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 9, size=0x6)})
    nLoop: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 10)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 11, count=2)})



@dataclass
class ParticleParamElement(PataponStaticDataClass, PataponDataClassElement):
    flag: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 0, size=0x8)})
    wait: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 1)})
    nPoly: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 2)})
    delay: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 3)})
    rdelay: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 4)})
    life: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 5)})
    rlife: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 6)})
    scale: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    rscale: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    tscale: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 10)})
    rspeed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 11)})
    tspeed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 12)})
    dirx: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 13)})
    rdirx: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 14)})
    diry: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 15)})
    rdiry: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 16)})
    dirz: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 17)})
    rdirz: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 18)})
    gravity: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 19)})
    anima_time: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 20)})
    anima_no: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 21)})
    nAnima: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 22)})
    rotx: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 23)})
    rotx_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 24)})
    roty: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 25)})
    roty_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 26)})
    rotz: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 27)})
    rotz_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 28)})
    crotx_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 29)})
    croty_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 30)})
    crotz_speed: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 31)})
    posx: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 32)})
    rposx: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 33)})
    posy: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 34)})
    rposy: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 35)})
    posz: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 36)})
    rposz: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 37)})
    rgba: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 38, size=0x4)})
    wave_x: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 39)})
    wave_y: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 40)})
    wave_z: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 41)})
    r_nPoly: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 42)})
    center_x: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 43)})
    center_y: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 44)})
    flag_ex: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 45)})
    escale: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 46)})
    tscale_key: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 47)})
    tscale_time: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 48)})
    talpha: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 49)})
    ealpha: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 50)})
    talpha_key: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 51)})
    talpha_time: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 52)})
    anima_pat: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 53, size=0x2)})
    center_z: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 54)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 55)})


@dataclass
class ParticleParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ParticleParamElement] = field(default_factory=list[ParticleParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("particle_param_count", "count")]})



@dataclass
class EffectKeySectionElement(PataponDynamicDataClass, PataponDataClassElement):
    key_data: EffectKeyData = field(default_factory=EffectKeyData, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("key_data", "header")]})
    particle_params: ParticleParam = field(default_factory=ParticleParam, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("key_data", "body")]})



@dataclass
class EffectKeySection(PataponDynamicDataClass, PataponDataClassElement):
    key_data_section_list: list[EffectKeySectionElement] = field(default_factory=list[EffectKeySectionElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("key_data_count", "count")]})



@dataclass
class EffectKey(PataponDynamicDataClass):
    header: EffectKeyHeader = field(default_factory=EffectKeyHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    effect_key_sections: EffectKeySection = field(default_factory=EffectKeySection, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})