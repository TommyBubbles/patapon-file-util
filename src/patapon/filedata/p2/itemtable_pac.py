from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


@dataclass
class ItemTableHeader(PataponStaticDataClass, PataponDataClassHeader):
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    categoryParamListOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("cat_offset", "source")]})
    filler_2: list[int] =field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=6)})



@dataclass
class ItemTableParamElement(PataponStaticDataClass, PataponDataClassElement):
    idOld: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 0)})
    id: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 1)})
    rarity: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 2)})
    subId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 3)})
    userValue: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 4)})
    categoryId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 5)})
    subCategoryId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 6)})
    userString: str = field(default="", metadata={"meta": FieldMetadata("string", 7, size=0x20)})
    iconModelName: str = field(default="", metadata={"meta": FieldMetadata("string", 8, size=0x20)})
    modelName: str = field(default="", metadata={"meta": FieldMetadata("string", 9, size=0x20)})
    iconScale: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 10)})
    iconOffsetY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 11)})
    OffsetY: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 12)})
    carrierId: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 13)})
    slotId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int16", 14)})
    nameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 15)})
    explainId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 16)})


def get_item_section_size(offset: int) -> int:
    return offset - ItemTableHeader().get_byte_size()


@dataclass
class ItemTableParam(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[ItemTableParamElement] = field(default_factory=list[ItemTableParamElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("cat_offset", "byte_size", func=get_item_section_size, func_params={"offset": "cat_offset"})]})



@dataclass
class CategoryParamListElement(PataponStaticDataClass, PataponDataClassElement):
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    NameId: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 1)})


@dataclass
class CategoryParamList(PataponDynamicDataClass, PataponDataClassBody):
    param_list: list[CategoryParamListElement] = field(default_factory=list[CategoryParamListElement], metadata={"meta": FieldMetadata("element_list", 0, count=10)})



@dataclass
class ItemTable(PataponDynamicDataClass):
    header: ItemTableHeader = field(default_factory=ItemTableHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    itemParamList: ItemTableParam = field(default_factory=ItemTableParam, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    categoryParamList: CategoryParamList = field(default_factory=CategoryParamList, metadata={"meta": FieldMetadata("body", 2)})