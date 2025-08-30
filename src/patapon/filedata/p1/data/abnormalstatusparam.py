from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


@dataclass
class AbnormalStatusParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("param_count", "source")]})
    param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 7, count=6)})



@dataclass
class AbnormalStatusParamElement():
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    priority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    isOneTime: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    useAbnormalMotionCtrl: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    funcId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    motionBaseType: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 7, count=2)})
    effectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    msgId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    reverseTiming: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    jumpTiming: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    damageBase: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    damageRand: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 15, count=4)})
    reverseTimingBase: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 16)})
    reverseTimingRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 17)})
    speed: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    jumpPower: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    jumpPowerRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 20)})
    damageTimingBase: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 21)})
    damageTimingRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 22)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x40)})


@dataclass
class AbnormalStatusParamList(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[AbnormalStatusParamElement] = field(default_factory=list[AbnormalStatusParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("param_count", "count")]})



@dataclass
class AbnormalStatusParam(PataponDynamicDataClass):
    header: AbnormalStatusParamHeader = field(default_factory=AbnormalStatusParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    params: AbnormalStatusParamList = field(default_factory=AbnormalStatusParamList, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})