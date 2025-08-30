if __name__ == '__main__':
    import sys
    sys.path.insert(0, ".\\src")

from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag
from patapon.filedata.p1.damageparam import DamageParam


@dataclass
class SquadActivityParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    offset1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    info_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    base_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("base_param_count", "source")]})
    base_param_element_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    missile_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("missile_param_count", "source")]})
    missile_param_element_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})



@dataclass
class BaseParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    scriptId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    enableCharaType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    filler_1: list[int]  = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=5)})
    ctrlFuncParamId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    attackRange: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    attackMoveRange: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    missileId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    rangeRatioAP: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 9)})
    rangeBackEnd: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    effectId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    isBrake: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 12)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x20)})
    str4: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x20)})
    str5: str = field(default="", metadata={"meta": FieldMetadata("string", 17, size=0x20)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 18)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("base_param_count", "count")]})



@dataclass
class MissileParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    initSpeed: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    initSpeedRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    degree: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    degreeRand: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    windRatio: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=3)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})


@dataclass
class MissileParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[MissileParamElement] = field(default_factory=list[MissileParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("missile_param_count", "count")]})



@dataclass
class SquadActivityParam(PataponDynamicDataClass):
    header: SquadActivityParamHeader = field(default_factory=SquadActivityParamHeader, metadata={"meta": FieldMetadata("header", 0, data_size=0x40), "tags": [FieldTag("file", "header")]})
    base_param: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    missile_param: MissileParam = field(default_factory=MissileParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})




if __name__ == '__main__':
    SquadActivityParam.verify_datafield_pos()

    with open("D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\squadactivityparam.dat", "rb") as file:
        raw = file.read()
        actual: SquadActivityParam = SquadActivityParam.from_bytes(raw)
        print(SquadActivityParam.verify_filler(actual))

    print(len(actual.base_param.param_list) == 0xD5)
    print(len(actual.missile_param.param_list) == 0x1B)

    with open(".\\squad_activity_damage_param.txt", "w") as output:
        output.write(f"{DamageParam().tsv_header()}\n")
        for i in actual.base_param.param_list:
            output.write(f"{i.damageParam.tsv()}\n")
            # print(f"{i.name} {i.enableCharaType} {i.ctrlFuncParamId}")

        for i in actual.missile_param.param_list:
            print(i.name)