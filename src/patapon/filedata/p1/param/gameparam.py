from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)
from .generic import GenericParamHeader



@dataclass
class GameParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("game_param_count", "source"))


@dataclass
class GameParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 1, count=24)})


@dataclass
class GameParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[GameParamInfoElement] = field(default_factory=list[GameParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("game_param_count", "count", 0)]})



@dataclass
class GameParam(PataponDynamicDataClass):
    header: GameParamHeader = field(default_factory=GameParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    game_params: GameParamInfo = field(default_factory=GameParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})



if __name__ == '__main__':
    test = GameParamHeader()
    field_info = test.__dataclass_fields__.get("partition_info_list", None)

    if field_info is not None:
        print(field_info.metadata.get("tags", None))
