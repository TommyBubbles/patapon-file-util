from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag
from patapon.filedata.p1.param import DamageParam



@dataclass
class CookingParamHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    cooking_param_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("cooking_param_count", "source")]})
    cooking_param_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 7, count=6)})



@dataclass
class CookingParamInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0x20)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    itemId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    damageParam: DamageParam = field(default_factory=DamageParam, metadata={"meta": FieldMetadata("body", 3)})


@dataclass
class CookingParamInfo(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CookingParamInfoElement] = field(default_factory=list[CookingParamInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("cooking_param_count", "count")]})



@dataclass
class CookingParam(PataponDynamicDataClass):
    header: CookingParamHeader = field(default_factory=CookingParamHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    chara_group_params: CookingParamInfo = field(default_factory=CookingParamInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})