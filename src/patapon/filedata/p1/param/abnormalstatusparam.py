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
class AbnormalStatusParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("abnormal_status_param_count", "source", 0, sub_tag))



@dataclass
class AbnormalStatusParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=6)})
    priority: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    isOneTime: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    useAbnormalMotionCtrl: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    funcId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    motionBaseType: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 8, count=2)})
    effectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    msgId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})
    reverseTiming: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})
    jumpTiming: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    damageBase: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    damageRand: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 16, count=4)})
    reverseTimingBase: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 17)})
    reverseTimingRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    speed: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    jumpPower: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 20)})
    jumpPowerRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 21)})
    damageTimingBase: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 22)})
    damageTimingRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 23)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 24)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 25, size=0x40)})


@dataclass
class AbnormalStatusParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[AbnormalStatusParamInfoElement] = field(default_factory=list[AbnormalStatusParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("abnormal_status_param_count", "count")]})



@dataclass
class AbnormalStatusParam(PataponDynamicDataClass):
    header: AbnormalStatusParamHeader = field(default_factory=AbnormalStatusParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    params: AbnormalStatusParamInfo = field(default_factory=AbnormalStatusParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})