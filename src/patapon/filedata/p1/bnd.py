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
class BNDHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: str = field(default="BND", metadata={"meta": FieldMetadata("string", 0, size=0x4)})
    flag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    alignSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    partitionInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    nameInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4), "tags": [FieldTag("nameInfoOffset", "source")]})
    dataTableOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("dataTableOffset", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 6, count=2)})
    nFiles: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    nPartitionInfo: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8), "tags": [FieldTag("partition_info_count", "source")]})
    


@dataclass
class PartitionInfoElement(PataponStaticDataClass, PataponDataClassElement):
    hash: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    nameOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    dataOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    dataSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("partition_size", "source")]})


@dataclass
class PartitionInfo(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[PartitionInfoElement] = field(default_factory=list[PartitionInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("partition_info_count", "count")]})


    def get_ordered_list(self, attr_name: str) -> list[PartitionInfoElement]:
        if attr_name in PartitionInfoElement.__dataclass_fields__.keys():
            return sorted(self.info_list, key=lambda x: getattr(x, attr_name))
        raise LookupError(f"Unable to find attribute {attr_name} in PartitionInfoElement")



@dataclass
class NameInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    nestLevel: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 0)})
    prevOffset: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 1)})
    nextOffset: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 2)})
    partitionOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 4, null_term=b'\x00')})


def data_size_from_offsets(start: int, end: int) -> int:
    return start - end


@dataclass
class NameInfo(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[NameInfoElement] = field(default_factory=list[NameInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("info_list_size", "size", func=data_size_from_offsets, func_params={"start": "nameInfoOffset", "end": "dataTableOffset"})]})



@dataclass
class Partitions(PataponDynamicDataClass, PataponDataClassBody):
    partition_list: list[bytes] = field(default_factory=list[bytes], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("dataSize", "size")]})



@dataclass
class BND(PataponDynamicDataClass):
    header: BNDHeader = field(default_factory=BNDHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    partition_info: PartitionInfo = field(default_factory=PartitionInfo, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
