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
class InstructionCommandParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("instruction_command_param_count", "source", 0, sub_tag))



@dataclass
class InstructionCommandParamInfoElement(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    instCommandId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 2)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=6)})
    commandType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    commandId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    soundCommandState: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})
    sqouadCommandLevelType: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 7)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 8, count=12)})


@dataclass
class InstructionCommandParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[InstructionCommandParamInfoElement] = field(default_factory=list[InstructionCommandParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("instruction_command_param_count", "count")]})



@dataclass
class InstructionCommandParam(PataponDynamicDataClass):
    header: InstructionCommandParamHeader = field(default_factory=InstructionCommandParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    instruction_command_params: InstructionCommandParamInfo = field(default_factory=InstructionCommandParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})