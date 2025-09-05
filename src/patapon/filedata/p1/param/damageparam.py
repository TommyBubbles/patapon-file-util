from enum import Enum
from dataclasses import dataclass, field
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    FieldMetadata,
)


class AttackEffectType(Enum):
    CRIT = 0
    KB = 1
    CNC = 2
    FIRE = 3
    SLEEP = 4
    UKN_1 = 5
    UKN_2 = 6
    UKN_3 = 7


@dataclass
class DamageParam(PataponStaticDataClass):
    hitPoint: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
    i1: float = field(default=0, metadata={"meta": FieldMetadata("float", 1)})
    moveSpeed: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    i2: float = field(default=0, metadata={"meta": FieldMetadata("float", 3)})
    attackWait: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    filler_3: float = field(default=0, metadata={"meta": FieldMetadata("float", 5)})
    knockBackDir: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    isWeapon: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    minBaseDamage: float = field(default=0, metadata={"meta": FieldMetadata("float", 8)})
    misslePierceFlag: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    maxBaseDamage: float = field(default=0, metadata={"meta": FieldMetadata("float", 10)})
    attackNBPower: float = field(default=0, metadata={"meta": FieldMetadata("float", 11)})
    sufferNBPower: float = field(default=0, metadata={"meta": FieldMetadata("float", 12)})
    hitSeFlag: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    attackFlag: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    materialID: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    attackRatio: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 16, count=8)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 17, size=0x20)})
    sufferDamageRatio: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 18, count=8)})
    sufferAttackAvoidanceRatio: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 19, count=8)})
    sufferAvoidRatio: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 20, count=8)})
    sufferInvalid: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 21, count=8)})