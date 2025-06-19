from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass, FieldMetadata

@dataclass
class CollisionParam(PataponStaticDataClass):
    file_name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="utf-8")})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    f2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    type: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20, encoding="utf-8")})
    s1: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20, encoding="utf-8")})