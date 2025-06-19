from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass, FieldMetadata

@dataclass
class ActorParam(PataponStaticDataClass):
    file_id: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="utf-8")})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x10, encoding="utf-8")})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 5, count=7)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20, encoding="utf-8")})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20, encoding="utf-8")})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20, encoding="utf-8")})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20, encoding="utf-8")})
    str6: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20, encoding="utf-8")})
    str7: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20, encoding="utf-8")})
    filler_3: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 12, count=24)})
    str8: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x20, encoding="utf-8")})
    str9: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x20, encoding="utf-8")})
    str10: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20, encoding="utf-8")})
    str11: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x20, encoding="utf-8")})