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
class BasesDataCharaParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("chara_param_count", "source", 0, sub_tag))



# used for charaparam.dat files from actor folder on a per actor basis
@dataclass
class CharaParam(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    charaType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3, count=1)})
    troopType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    mtpCategoryId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    modelDirection: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    callStatusScript: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    charNameId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    effectId_fire: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    offsetX_fire: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    offsetY_fire: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 12)})
    nodeName_fire: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x10)})
    effectId_sleep: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 14)})
    offsetX_sleep: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 15)})
    offsetY_sleep: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 16)})
    filler_3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 17)})
    nodeName_sleep: str = field(default="", metadata={"meta": FieldMetadata("string", 18, size=0x10)})
    aSeTable: list[bytes] = field(default_factory=list[bytes], metadata={"meta": FieldMetadata("bytes", 19, count=16, size=4)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 20, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 21, size=0x20)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("dataclass", 22)})
    modelFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 23, size=0x20)})
    actorName: str = field(default="", metadata={"meta": FieldMetadata("string", 24, size=0x20)})
    charaname: str = field(default="", metadata={"meta": FieldMetadata("string", 25, size=0x20, encoding="shift-jis")})
    equipFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 26, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 27, size=0x20)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 28, size=0x20)})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 29, size=0x20)})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 30, count=8)})
    str6: str = field(default="", metadata={"meta": FieldMetadata("string", 31, size=0x20)})
    filler_5: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 32, count=56)})


@dataclass
class CharaParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CharaParam] = field(default_factory=list[CharaParam], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("chara_param_count", "count")]})



@dataclass
class BasesDataCharaParam(PataponDynamicDataClass):
    header: BasesDataCharaParamHeader = field(default_factory=BasesDataCharaParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    chara_params: CharaParamInfo = field(default_factory=CharaParamInfo, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
