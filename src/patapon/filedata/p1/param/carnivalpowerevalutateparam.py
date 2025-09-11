from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from .generic import GenericParamHeader



# Note: there is a value at 0x38 (0x30) that is not captured by this class.
#       it is unclear as of right now if this will cause issues in the future
@dataclass
class CarnivalPowerEvalutateParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("cpep_global_settings_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("cpep_regular_settings_count", "source", 1, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("cpep_common_param_count", "source", 2, sub_tag))



@dataclass
class CarnivalPowerEvalutateGlobalSettingsElement(PataponStaticDataClass, PataponDataClassElement):
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
class CarnivalPowerEvalutateGlobalSettings(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[CarnivalPowerEvalutateGlobalSettingsElement] = field(default_factory=list[CarnivalPowerEvalutateGlobalSettingsElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("cpep_global_settings_count", "count")]})



@dataclass
class CarnivalPowerEvalutateRegularSettingsElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    blueBonusRate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    excellentBonusScore: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    nextBonus: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    chainBonus: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    chainCount: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    addLastPointRate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})
    maxEVPoint: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 8)})
    maxComboScore: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    addComboScoreRate: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    hightEVPoint: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    lastLevelPoint: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 12)})


@dataclass
class CarnivalPowerEvalutateRegularSettings(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[CarnivalPowerEvalutateRegularSettingsElement] = field(default_factory=list[CarnivalPowerEvalutateRegularSettingsElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("cpep_regular_settings_count", "count")]})



@dataclass
class CarnivalPowerEvalutateCommonParamElement(PataponStaticDataClass, PataponDataClassElement):
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
class CarnivalPowerEvalutateCommonParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CarnivalPowerEvalutateCommonParamElement] = field(default_factory=list[CarnivalPowerEvalutateCommonParamElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("cpep_common_param_count", "count")]})



@dataclass
class CarnivalPowerEvalutateParam(PataponDynamicDataClass):
    header: CarnivalPowerEvalutateParamHeader = field(default_factory=CarnivalPowerEvalutateParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    global_settings: CarnivalPowerEvalutateGlobalSettings = field(default_factory=CarnivalPowerEvalutateGlobalSettings, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    regular_settings: CarnivalPowerEvalutateRegularSettings = field(default_factory=CarnivalPowerEvalutateRegularSettings, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
    common_params: CarnivalPowerEvalutateCommonParam = field(default_factory=CarnivalPowerEvalutateCommonParam, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("file", "body")]})