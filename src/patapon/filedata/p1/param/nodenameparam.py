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
class NodeNameParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        sub_tag = FieldTag("element_count", "source")
        cls.add_tag_to_field("partition_info_list", FieldTag("nn_unit_1_param_count", "source", 0, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("nn_unit_2_param_count", "source", 1, sub_tag))
        cls.add_tag_to_field("partition_info_list", FieldTag("nn_equip_param_count", "source", 2, sub_tag))


# used by defaultEquipList
@dataclass
class NodeName(PataponStaticDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    charaType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    equipType: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    str1: str = field(default="", metadata={"meta": FieldMetadata("string", 6, size=0x20)})
    str2: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    category: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    targetType: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    nodeName: str = field(default="", metadata={"meta": FieldMetadata("string", 10, size=0x20)})
    str3: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x20)})


@dataclass
class Unit1NodeNameParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[NodeName] = field(default_factory=list[NodeName], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("nn_unit_1_param_count", "count")]})


@dataclass
class Unit2NodeNameParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[NodeName] = field(default_factory=list[NodeName], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("nn_unit_2_param_count", "count")]})


@dataclass
class EquipNodeNameParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[NodeName] = field(default_factory=list[NodeName], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("nn_equip_param_count", "count")]})



@dataclass
class NodeNameParam(PataponDynamicDataClass):
    header: NodeNameParamHeader = field(default_factory=NodeNameParamHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    unit_1_params: Unit1NodeNameParam = field(default_factory=Unit1NodeNameParam, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    unit_2_params: Unit2NodeNameParam = field(default_factory=Unit2NodeNameParam, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
    equip_params: EquipNodeNameParam = field(default_factory=EquipNodeNameParam, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("file", "body")]})