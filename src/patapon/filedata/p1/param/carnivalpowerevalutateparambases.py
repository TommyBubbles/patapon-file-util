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



# Note: there is a value at 0x48 (0x30) that is not captured by this class.
#       it is unclear as of right now if this will cause issues in the future
@dataclass
class CarnivalPowerEvalutateParamBasesHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("global_settings_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("regular_settings_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("common_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("unknown_1_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("unknown_2_param_count", "source"))



@dataclass
class GlobalSettingsParamElement(PataponStaticDataClass, PataponDataClassElement):
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
class GlobalSettingsParam(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[GlobalSettingsParamElement] = field(default_factory=list[GlobalSettingsParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("global_settings_count", "count", 0)]})



@dataclass
class RegularSettingsParamElement(PataponStaticDataClass, PataponDataClassElement):
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
class RegularSettingsParam(PataponDynamicDataClass, PataponDataClassBody):
    settings_list: list[RegularSettingsParamElement] = field(default_factory=list[RegularSettingsParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("regular_settings_count", "count", 1)]})



@dataclass
class CommonParamElement(PataponStaticDataClass, PataponDataClassElement):
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
class CommonParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CommonParamElement] = field(default_factory=list[CommonParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("common_param_count", "count", 2)]})



@dataclass
class Unknown1ParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=2)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
    f2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})
    f3: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 6)})
    f4: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 7)})


@dataclass
class Unknown1Param(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[Unknown1ParamElement] = field(default_factory=list[Unknown1ParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("unknown_1_param_count", "count", 3)]})



@dataclass
class Unknown2ParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    f1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=6)})


@dataclass
class Unknown2Param(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[Unknown2ParamElement] = field(default_factory=list[Unknown2ParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("unknown_2_param_count", "count", 4)]})



@dataclass
class CarnivalPowerEvalutateParamBases(PataponDynamicDataClass):
    header: CarnivalPowerEvalutateParamBasesHeader = field(default_factory=CarnivalPowerEvalutateParamBasesHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    global_settings: GlobalSettingsParam = field(default_factory=GlobalSettingsParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    regular_settings: RegularSettingsParam = field(default_factory=RegularSettingsParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    common_params: CommonParam = field(default_factory=CommonParam, metadata={"meta": FieldMetadata("body", 3), "tags": [FieldTag("file", "body")]})
    unknown_1: Unknown1Param = field(default_factory=Unknown1Param, metadata={"meta": FieldMetadata("body", 4), "tags": [FieldTag("file", "body")]})
    unknown_2: Unknown2Param = field(default_factory=Unknown2Param, metadata={"meta": FieldMetadata("body", 5), "tags": [FieldTag("file", "body")]})