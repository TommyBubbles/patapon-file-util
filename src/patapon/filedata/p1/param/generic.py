from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponDynamicDataClass, PataponStaticDataClass, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


def align_header(partition_count: int, alignment: int):
    base_header_size = 0x20
    partition_info_size = 0x8 * partition_count
    total_size = base_header_size + partition_info_size
    return alignment - (total_size % alignment)


@dataclass
class GenericParamHeaderParitionInfo(PataponStaticDataClass, PataponDataClassElement):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("element_count", "source")]})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class GenericParamHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: str = field(default="YGF_GFP\x00", metadata={"meta": FieldMetadata("string", 0, size=0x8)})
    alignment: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("alignment", "source")]})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("partition_count", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    partition_info_list: list[GenericParamHeaderParitionInfo] = field(default_factory=list[GenericParamHeaderParitionInfo], metadata={"meta": FieldMetadata("element_list", 5), "tags": [FieldTag("partition_count", "count")]})
    padding: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 6), "tags": [FieldTag("padding", "size", func=align_header, func_params={"partition_count": "partition_count", "alignment": "alignment"})]})
