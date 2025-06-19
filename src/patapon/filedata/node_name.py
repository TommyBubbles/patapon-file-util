from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass, FieldMetadata

@dataclass
class NodeNameParam(PataponStaticDataClass):
    file_name: str = field(default='', metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="utf-8")})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    s1: str = field(default='', metadata={"meta": FieldMetadata("string", 6, size=0x20, encoding="utf-8")})
    s2: str = field(default='', metadata={"meta": FieldMetadata("string", 7, size=0x20, encoding="utf-8")})
    s3: str = field(default='', metadata={"meta": FieldMetadata("string", 8, size=0x20, encoding="utf-8")})
    node_name: str = field(default='', metadata={"meta": FieldMetadata("string", 9, size=0x20, encoding="utf-8")})
    node_type: str = field(default='', metadata={"meta": FieldMetadata("string", 10, size=0x20, encoding="utf-8")})
    s4: str = field(default='', metadata={"meta": FieldMetadata("string", 11, size=0x20, encoding="utf-8")})