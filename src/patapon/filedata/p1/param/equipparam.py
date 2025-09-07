from dataclasses import dataclass, field
from patapon.filedata.patapon_data_class import PataponStaticDataClass, FieldMetadata
from . import DamageParam



@dataclass
class EquipParam(PataponStaticDataClass):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list, metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    itemId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    categoryId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    useCharaId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    troopId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    shotEffectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=7)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 9)})
    modelFileName: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    effectModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})