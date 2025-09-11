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
class SoundGameParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("sound_game_param_count", "source", 0, sub_tag))



@dataclass
class SoundGameParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filename: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x40)})


@dataclass
class SoundGameParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[SoundGameParamInfoElement] = field(default_factory=list[SoundGameParamInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("sound_game_param_count", "count")]})



@dataclass
class SoundGameParam(PataponDynamicDataClass):
    header: SoundGameParamHeader = field(default_factory=SoundGameParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    sound_game_params: SoundGameParamInfo = field(default_factory=SoundGameParamInfo, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
