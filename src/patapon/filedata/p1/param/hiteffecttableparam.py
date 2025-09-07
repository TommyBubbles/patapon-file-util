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
class HitEffectTableParamHeader(GenericParamHeader):
    @classmethod
    def add_tags(cls):
        cls.add_tag_to_field("partition_info_list", FieldTag("base_param_count", "source"))
        cls.add_tag_to_field("partition_info_list", FieldTag("attack_material_table_count", "source"))



@dataclass
class BaseParamElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20, encoding="shift-jis")})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=3)})
    effectScriptLabelId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 3)})
    sufferScriptLabelId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    userId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})
    useDefaultTable: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 6)})


@dataclass
class BaseParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[BaseParamElement] = field(default_factory=list[BaseParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("base_param_count", "count", 0)]})



@dataclass
class AttackMaterialTableElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    indexId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 2, count=7)})
    materialTable: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("signed_int", 3, count=16)})


@dataclass
class AttackMaterialTable(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[AttackMaterialTableElement] = field(default_factory=list[AttackMaterialTableElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("attack_material_table_count", "count", 1)]})



@dataclass
class HitEffectTableParam(PataponDynamicDataClass):
    header: HitEffectTableParamHeader = field(default_factory=HitEffectTableParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    base_params: BaseParam = field(default_factory=BaseParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    attack_material_table: AttackMaterialTable = field(default_factory=AttackMaterialTable, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})