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
class SquadLineParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("squad_line_param_count", "source"))



@dataclass
class TierLevelParam(PataponStaticDataClass):
    front: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 0)})
    middle: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    back: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})



@dataclass
class EachCharaParam(PataponDynamicDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    priority: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 1)})
    position: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 2)})
    inst_move: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 3)})
    inst_shortRange: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 4)})
    inst_longRange: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 5)})
    inst_charge: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 6)})
    inst_escape: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 7)})
    inst_rsv5: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 8)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})



@dataclass
class ActivityTableParam(PataponDynamicDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    priority: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 1)})
    position: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 2)})
    instruction: list[TierLevelParam] = field(default_factory=list[TierLevelParam], metadata={"meta": FieldMetadata("element_list", 3, count=5)})
    inst_rsv5: TierLevelParam = field(default_factory=TierLevelParam, metadata={"meta": FieldMetadata("body", 4)})
    rsv1: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x20)})
    rsv2: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    rsv3: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})



@dataclass
class SquadLineParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    rsv: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    view: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    speedRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 5, count=4)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    str6: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})
    eachCharaData: list[EachCharaParam] = field(default_factory=list[EachCharaParam], metadata={"meta": FieldMetadata("element_list", 12, count=8)})
    activityTable: list[ActivityTableParam] = field(default_factory=list[ActivityTableParam], metadata={"meta": FieldMetadata("element_list", 13, count=32)})


@dataclass
class SquadLineParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[SquadLineParamInfoElement] = field(default_factory=list[SquadLineParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("squad_line_param_count", "count", 0)]})



@dataclass
class SquadLineParam(PataponDynamicDataClass):
    header: SquadLineParamHeader = field(default_factory=SquadLineParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    squad_line_params: SquadLineParamInfo = field(default_factory=SquadLineParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
