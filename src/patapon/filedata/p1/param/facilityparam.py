from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassBody,
    PataponDataClassHeader,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)



@dataclass
class FacilityParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    id: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    header_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    section_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    param_list_element_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("param_list_count", "source")]})
    param_list_element_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    model_param_list_element_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("model_param_list_count", "source")]})
    model_param_list_element_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8)})
    attach_param_list_element_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9), "tags": [FieldTag("attach_param_list_count", "source")]})
    attach_param_list_element_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})



@dataclass
class FacilityParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    poolSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    scriptName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    modelName_1: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    pri_1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    seedCost_1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    personalCost_1: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    modelName_2: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    pri_2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 9)})
    seedCost_2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 10)})
    personalCost_2: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 11)})
    modelName_3: str = field(default="", metadata={"meta": FieldMetadata("string", 12, size=0x20)})
    pri_3: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 13)})
    seedCost_3: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 14)})
    personalCost_3: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    type: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 16)})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 17, size=0x8)})


@dataclass
class FacilityParamList(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[FacilityParamElement] = field(default_factory=list[FacilityParamElement], metadata={"meta": FieldMetadata("element", 0), "tags": [FieldTag("param_list_count", "count")]})



@dataclass
class FacilityModelParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 1, size=0x20)})
    buildName: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x20)}) # wreckName
    resourceType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)}) # nAttach
    attachName_1: str = field(default="", metadata={"meta": FieldMetadata("string", 5, size=0x20)})
    attachName_2: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    attachName_3: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    attachName_4: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    attachName_5: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    attachName_6: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    width: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    nBuildMotionParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 12)})
    nWreckMotionParam: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 13)})
    startFrame_1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 14)})
    nFrame_1: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 15)})
    startFrame_2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 16)})
    nFrame_2: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 17)})
    startFrame_3: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 18)})
    nFrame_3: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 19)})
    startFrame_4: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 20)})
    nFrame_4: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 21)})
    startFrame_5: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 22)})
    nFrame_5: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 23)})
    startFrame_6: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 24)})
    nFrame_6: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 25)})
    startFrame_7: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 26)})
    nFrame_7: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 27)})
    startFrame_8: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 28)})
    nFrame_8: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 29)})
    startFrame_9: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 30)})
    nFrame_9: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 31)})


@dataclass
class FacilityModelParamList(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[FacilityModelParamElement] = field(default_factory=list[FacilityModelParamElement], metadata={"meta": FieldMetadata("element", 0), "tags": [FieldTag("model_param_list_count", "count")]})



@dataclass
class FacilityAttachParamElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    nAttach: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    modelAttachNodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 2, size=0x20)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})
    particleAttachNodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})
    particleId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    isEnableSearch: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})


@dataclass
class FacilityAttachParamList(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[FacilityAttachParamElement] = field(default_factory=list[FacilityAttachParamElement], metadata={"meta": FieldMetadata("element", 0), "tags": [FieldTag("attach_param_list_count", "count")]})



# used by personparam
@dataclass
class FacilityParam(PataponDynamicDataClass):
    header: FacilityParamHeader = field(default_factory=FacilityParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    facilityParamList: FacilityParamList = field(default_factory=FacilityParamList, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    facilityModelParamList: FacilityModelParamList = field(default_factory=FacilityModelParamList, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})
    facilityAttachParamList: FacilityAttachParamList = field(default_factory=FacilityAttachParamList, metadata={"meta": FieldMetadata("body", 3), "tags": [FieldTag("file", "body")]})