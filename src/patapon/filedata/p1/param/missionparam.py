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
class SystemDataMissionParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("mission_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("extra_param_count", "source"))



# used by mission specific missionparam.dat files
@dataclass
class MissionParam(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    nextLinkId: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=16)})
    aMessageFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x40)})
    aStageFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x40)})
    aUnitFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x40)})
    aScriptFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x40)})
    aSoundFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x40)})
    aMapFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x40)})
    reserve_1: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x40)})
    reserve_2: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x40)})
    reserve_3: str = field(default="", metadata={"meta": FieldMetadata("string", 12, size=0x40)})
    reserve_4: str = field(default="", metadata={"meta": FieldMetadata("string", 13, size=0x40)})
    reserve_5: str = field(default="", metadata={"meta": FieldMetadata("string", 14, size=0x40)})
    reserve_6: str = field(default="", metadata={"meta": FieldMetadata("string", 15, size=0x40)})
    reserve_7: str = field(default="", metadata={"meta": FieldMetadata("string", 16, size=0x40)})
    reserve_8: str = field(default="", metadata={"meta": FieldMetadata("string", 17, size=0x40)})


@dataclass
class MissionParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[MissionParam] = field(default_factory=list[MissionParam], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("mission_param_count", "count", 0)]})



@dataclass
class SystemDataMissionParamExtraParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=7)})
    aMapFilename: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x40)})
    text: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x40, encoding="shift-jis")})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=16)})


@dataclass
class SystemDataMissionParamExtraParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[SystemDataMissionParamExtraParamElement] = field(default_factory=list[SystemDataMissionParamExtraParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("extra_param_count", "count", 0)]})



@dataclass
class SystemDataMissionParam(PataponDynamicDataClass):
    header: SystemDataMissionParamHeader = field(default_factory=SystemDataMissionParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    mission_params: MissionParamInfo = field(default_factory=MissionParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    extra_params: SystemDataMissionParamExtraParam = field(default_factory=SystemDataMissionParamExtraParam, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
