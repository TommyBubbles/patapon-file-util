from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    FieldMetadata
)



@dataclass
class CollisionParam(PataponStaticDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    collisionType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    offsetX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    offsetY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    sizeX: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    sizeY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    userId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    hitCategoryType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    nodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})