from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, FieldMetadata

@dataclass
class MissionParam(PataponStaticDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    indexId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    aMessageFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x40)})
    aStageFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x40)})
    aUnitFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x40)})
    aScriptFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x40)})
    aSoundFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x40)})
    aMepFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x40)})
    reserve_1: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x40)})
    reserve_2: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x40)})
    reserve_3: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x40)})
    reserve_4: str = field(default="", metadata={"meta": FieldMetadata("string", 12, size=0x40)})
    reserve_5: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x40)})
    reserve_6: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x40)})
    reserve_7: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x40)})
    reserve_8: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x40)})