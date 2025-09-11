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
class MiracleParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("miracle_param_count", "source", 0, sub_tag))


@dataclass
class MiracleParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    itemId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    filename: str = field(default="", metadata={"meta": FieldMetadata("string", 3, size=0x20)})


@dataclass
class MiracleParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[MiracleParamInfoElement] = field(default_factory=list[MiracleParamInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("miracle_param_count", "count")]})



@dataclass
class MiracleParam(PataponDynamicDataClass):
    header: MiracleParamHeader = field(default_factory=MiracleParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    miracle_params: MiracleParamInfo = field(default_factory=MiracleParamInfo, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
