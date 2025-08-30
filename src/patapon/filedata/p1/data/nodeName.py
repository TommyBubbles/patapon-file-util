from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, FieldMetadata

# used by defaultEquipList as well
@dataclass
class NodeName(PataponStaticDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    charaType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    equipType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    category: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    targetType: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    nodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})