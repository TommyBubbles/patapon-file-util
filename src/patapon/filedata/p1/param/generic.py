from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponDynamicDataClass,
    PataponStaticDataClass,
    PataponDataClassHeader,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag
)



def align_header(partition_count: int, alignment: int):
    base_header_size = 0x20
    partition_info_size = 0x8 * partition_count
    total_size = base_header_size + partition_info_size
    if total_size % alignment == 0:
        return 0
    return alignment - (total_size % alignment)


@dataclass
class GenericParamHeaderPartitionInfo(PataponStaticDataClass, PataponDataClassElement):
    count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("element_count", "source")]})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class GenericParamHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: bytes = field(default=b"YGF_GFP", metadata={"meta": FieldMetadata("bytes", 0, size=0x8)})
    alignment: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("alignment", "source")]})
    version: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    partition_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("partition_count", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})
    partition_info_list: list[GenericParamHeaderPartitionInfo] = field(default_factory=list[GenericParamHeaderPartitionInfo], metadata={"meta": FieldMetadata("dataclass", 5), "tags": [FieldTag("partition_count", "count")]})
    padding: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 6), "tags": [FieldTag("padding", "size", func=align_header, func_params={"partition_count": "partition_count", "alignment": "alignment"})]})


    @classmethod
    def add_tags(cls): ...


    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.add_tags()
        return instance
