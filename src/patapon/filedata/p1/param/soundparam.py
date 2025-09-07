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



@dataclass
class SoundParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("mood_setting_param", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("antecedent_def_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("rule_def_param_count", "source"))



@dataclass
class MoodSettingParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    lvUpperBoundMorale: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 2, count=3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=4)})


@dataclass
class MoodSettingParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[MoodSettingParamElement] = field(default_factory=list[MoodSettingParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("sound_game_param_count", "count", 0)]})



@dataclass
class AntecedentDefParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    condId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    arg: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 3, count=4)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 4, count=2)})


@dataclass
class AntecedentDefParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[AntecedentDefParamElement] = field(default_factory=list[AntecedentDefParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("antecedent_def_param_count", "count", 1)]})



@dataclass
class RuleDefParamElement(PataponStaticDataClass, PataponDataClassElement):
    aName: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    antecedentId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=6)})
    registCommand: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 4, count=7)})


@dataclass
class RuleDefParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[RuleDefParamElement] = field(default_factory=list[RuleDefParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("rule_def_param_count", "count", 2)]})



@dataclass
class SoundParam(PataponDynamicDataClass):
    header: SoundParamHeader = field(default_factory=SoundParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    mood_setting_params: MoodSettingParam = field(default_factory=MoodSettingParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    antecedent_def_params: AntecedentDefParam = field(default_factory=AntecedentDefParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    rule_def_params: RuleDefParam = field(default_factory=RuleDefParam, metadata={"meta": FieldMetadata("body", 3), "tags": [FieldTag("file", "body")]})
