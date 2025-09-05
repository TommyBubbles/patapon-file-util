from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag



@dataclass
class CharaGroupParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    chara_group_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("chara_group_param_count", "source")]})
    chara_group_param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 7, count=6)})



@dataclass
class CharaGroupParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    rsv2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=6)})
    charaFlag: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 4, count=16)})


@dataclass
class CharaGroupParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CharaGroupParamInfoElement] = field(default_factory=list[CharaGroupParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("chara_group_param_count", "count")]})



@dataclass
class CharaGroupParam(PataponDynamicDataClass):
    header: CharaGroupParamHeader = field(default_factory=CharaGroupParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    chara_group_params: CharaGroupParamInfo = field(default_factory=CharaGroupParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})