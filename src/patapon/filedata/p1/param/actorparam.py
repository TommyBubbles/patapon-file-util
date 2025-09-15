from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    FieldMetadata
)



@dataclass
class ActorParam(PataponStaticDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="utf-8")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x10, encoding="utf-8")})
    categoryId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    isUseModel: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    isUseDamage: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    isUseCollision: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    isUseScript: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    isUseMsg: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20, encoding="utf-8")})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 12, size=0x20, encoding="utf-8")})
    damageParamName: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x20, encoding="utf-8")})
    scriptName: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x20, encoding="utf-8")})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20, encoding="utf-8")})
    localDataName: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x20, encoding="utf-8")})
    filler_3: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 17, count=24)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 18, size=0x20, encoding="utf-8")})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 19, size=0x20, encoding="utf-8")})
    str6: str = field(default="", metadata={"meta": FieldMetadata("string", 20, size=0x20, encoding="utf-8")})
    str7: str = field(default="", metadata={"meta": FieldMetadata("string", 21, size=0x20, encoding="utf-8")})