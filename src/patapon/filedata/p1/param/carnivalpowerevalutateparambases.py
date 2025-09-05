from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


@dataclass
class CarnivalPowerEvalutateParamBasesHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    global_settings_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("global_settings_count", "source")]})
    global_settings_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    regular_settings_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("regular_settings_count", "source")]})
    regular_settings_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    common_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9), "tags": [FieldTag("common_param_count", "source")]})
    common_param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    unknown_1_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 11), "tags": [FieldTag("unknown_1_count", "source")]})
    unknown_1_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 12)})
    unknown_2_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 13), "tags": [FieldTag("unknown_2_count", "source")]})
    unknown_2_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 14)})
    unknown_3_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 15), "tags": [FieldTag("unknown_3_count", "source")]})
    unknown_3_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 16)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 17, count=12)})



@dataclass
class CarnivalPowerEvalutateParamBasesGlobalSettingsElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    gameStartCP: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    canDamageCP: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    maxCP: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    maxBeatEV: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    allBlueMag: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    oneRhythmChainBonus: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    threeRhythmChainBonus: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    lastRhythmEVMag: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 9)})
    maxRhythmEV: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    rhythmFailedEV: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    reserved: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})


@dataclass
class CarnivalPowerEvalutateParamBasesGlobalSettings(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[CarnivalPowerEvalutateParamBasesGlobalSettingsElement] = field(default_factory=list[CarnivalPowerEvalutateParamBasesGlobalSettingsElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("global_settings_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParamBasesRegularSettingsElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    blueBonusRate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    excellentBonusScore: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    nextBonus: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    chainCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    addLastPointRate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    maxEVPoint: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    hightEVPoint: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})


@dataclass
class CarnivalPowerEvalutateParamBasesRegularSettings(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[CarnivalPowerEvalutateParamBasesRegularSettingsElement] = field(default_factory=list[CarnivalPowerEvalutateParamBasesRegularSettingsElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("regular_settings_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParamBasesCommonParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    command: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    detail: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    nageId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    kaesiId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    commandType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    useType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    padding: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    key: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int16", 9, count=8)})


@dataclass
class CarnivalPowerEvalutateParamBasesCommonParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CarnivalPowerEvalutateParamBasesCommonParamElement] = field(default_factory=list[CarnivalPowerEvalutateParamBasesCommonParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("common_param_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParamBasesUnknown1Element(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=2)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    f2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    f3: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    f4: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})


@dataclass
class CarnivalPowerEvalutateParamBasesUnknown1(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CarnivalPowerEvalutateParamBasesUnknown1Element] = field(default_factory=list[CarnivalPowerEvalutateParamBasesUnknown1Element], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("unknown_1_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParamBasesUnknown2Element(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=6)})


@dataclass
class CarnivalPowerEvalutateParamBasesUnknown2(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CarnivalPowerEvalutateParamBasesUnknown2Element] = field(default_factory=list[CarnivalPowerEvalutateParamBasesUnknown2Element], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("unknown_2_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParamBases(PataponDynamicDataClass):
    header: CarnivalPowerEvalutateParamBasesHeader = field(default_factory=CarnivalPowerEvalutateParamBasesHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    global_settings: CarnivalPowerEvalutateParamBasesGlobalSettings = field(default_factory=CarnivalPowerEvalutateParamBasesGlobalSettings, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    regular_settings: CarnivalPowerEvalutateParamBasesRegularSettings = field(default_factory=CarnivalPowerEvalutateParamBasesRegularSettings, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    common_params: CarnivalPowerEvalutateParamBasesCommonParam = field(default_factory=CarnivalPowerEvalutateParamBasesCommonParam, metadata={"meta": FieldMetadata("body", 3), "tags": [FieldTag("file", "body")]})
    unknown_1: CarnivalPowerEvalutateParamBasesUnknown1 = field(default_factory=CarnivalPowerEvalutateParamBasesUnknown1, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("file", "body")]})
    unknown_2: CarnivalPowerEvalutateParamBasesUnknown2 = field(default_factory=CarnivalPowerEvalutateParamBasesUnknown2, metadata={"meta": FieldMetadata("body", 5), "tags": [FieldTag("file", "body")]})