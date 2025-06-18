from dataclasses import dataclass, field
from .patapon_data_class import PataponStaticDataClass, FieldMetadata


@dataclass
class EquipParam(PataponStaticDataClass):
    internal_name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="utf-8")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=4)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    filler_3: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 7, count=2)})
    i4: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    filler_4: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 9, count=20)})
    model_name: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20, encoding="utf-8")})
    filler_5: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 11, count=8)})