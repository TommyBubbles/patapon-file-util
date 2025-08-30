from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


@dataclass
class BNDHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: str = field(default="BND", metadata={"meta": FieldMetadata("string", 0, size=0x4)})
    flag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    alignSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    partitionInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    nameInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4), "tags": [FieldTag("nameInfoOffset", "source")]})
    dataTableOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("dataTableOffset", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 6, count=2)})
    


@dataclass
class PartitionInfoHeader(PataponStaticDataClass, PataponDataClassHeader):
    nFiles: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    nPartitionInfo: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("nPartitionInfo", "source")]})


@dataclass
class PartitionInfoElement(PataponStaticDataClass, PataponDataClassElement):
    hash: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    nameOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    dataOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    dataSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("dataSize", "source")]})


@dataclass
class PartitionInfo(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[PartitionInfoElement] = field(default_factory=list[PartitionInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("nPartitionInfo", "count")]})


    def ordered_by_attribute(self, attr_name: str) -> list[PartitionInfoElement]:
        func = lambda x: getattr(x, attr_name)
        ordered_list = sorted(self.info_list, key=func)
        return ordered_list



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
    info_list: list[NameInfoElement] = field(default_factory=list[NameInfoElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("info_list_size", "byte_size", func=data_size_from_offsets, func_params={"start": "nameInfoOffset", "end": "dataTableOffset"})]})



@dataclass
class Partitions(PataponDynamicDataClass, PataponDataClassBody):
    partition_list: list[bytes] = field(default_factory=list[bytes], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("dataSize", "data_size")]})



@dataclass
class BND(PataponDynamicDataClass):
    header: BNDHeader
    partition_info_header: PartitionInfoHeader
    partition_info: PartitionInfo
    name_info: NameInfo
    partitions: Partitions
