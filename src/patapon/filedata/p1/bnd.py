from dataclasses import dataclass, field
from zlib import crc32
from typing import Literal
from patapon.filedata.patapon_data_class import (
    PataponDataClass,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    PataponDataClassHeader,
    PataponDataClassElement,
    FieldMetadata,
    FieldTag,
    PataponDataIO
)
import patapon.filedata.p1.param as param
from .unknown import UnknownDataClass
from .param.generic import GenericParamHeader
from .gxx import GxxHeader, Gxx
from .gxt import GXTHeader, GXT
from .effectkey import EffectKeyHeader, EffectKey



@dataclass
class PartitionInfo(PataponStaticDataClass, PataponDataClassElement):
    hash: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    nameOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    dataOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    dataSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("partition_size", "source")]})


def get_filename_size(element_size: int) -> int:
    if element_size == -1:
        return 1
    return element_size - 7


@dataclass
class NameInfo(PataponDynamicDataClass, PataponDataClassElement):
    nestLevel: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 0)})
    prevOffset: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 1)})
    nextOffset: int = field(default=0, metadata={"meta": FieldMetadata("signed_int8", 2), "tags": [FieldTag("element_size", "source"), FieldTag("next_name_info_element", "source")]})
    partitionOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 4), "tags": [FieldTag("filename_size", "size", func=get_filename_size, func_params={"element_size": "element_size"})]})


    def calc_hash(self):
        striped_name = self.name.strip('\x00')
        return crc32(striped_name.encode())


def has_next_element(next: int, file_count: int) -> bool:
    return next != -1 and file_count > 0


def align_header(alignment: int, obj: PataponDataClass):
    return alignment - (obj.get_byte_size(0, 11) % alignment)


@dataclass
class BNDHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: bytes = field(default=b"BND", metadata={"meta": FieldMetadata("bytes", 0, size=0x4)})
    flag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    alignSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("alignment", "source")]})
    partitionInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    nameInfoOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4), "tags": [FieldTag("nameInfoOffset", "source")]})
    dataTableOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("dataTableOffset", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 6, count=2)})
    nFiles: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("file_count", "source")]})
    nPartitionInfo: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8), "tags": [FieldTag("partition_info_count", "source")]})
    partition_info: list[PartitionInfo] = field(default_factory=list[PartitionInfo], metadata={"meta": FieldMetadata("dataclass", 9), "tags": [FieldTag("partition_info_count", "count")]})
    name_info: list[NameInfo] = field(default_factory=list[NameInfo], metadata={"meta": FieldMetadata("dataclass", 10), "tags": [FieldTag("next_element", "linked_list", func=has_next_element, func_params={"next": "next_name_info_element", "file_count": "file_count"}), FieldTag("name_info", "source")]})
    padding: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 11), "tags": [FieldTag("padding", "size", func=align_header, func_params={"alignment": "alignment", "obj": "self"})]})


    def get_ordered_partition_info(self, order_name: str, filter_name: str | None = None) -> list[PartitionInfo]:
        if order_name in PartitionInfo.__dataclass_fields__.keys():
            if filter_name is not None and filter_name in PartitionInfo.__dataclass_fields__.keys():
                filtered_info_list = filter(lambda x: getattr(x, filter_name) != 0, self.partition_info)
                ordered_info_list = sorted(filtered_info_list, key=lambda x: getattr(x, order_name))
            else:
                ordered_info_list = sorted(self.partition_info, key=lambda x: getattr(x, order_name))

            return ordered_info_list
        raise LookupError(f"Unable to find attribute {order_name} in PartitionInfo")
    

    def get_ordered_name_info(self, order_name: str, filter_name: str = "") -> list[NameInfo]:
        if order_name in NameInfo.__dataclass_fields__.keys():
            if filter_name in NameInfo.__dataclass_fields__.keys():
                filtered_info_list = filter(lambda x: getattr(x, filter_name) != 0, self.name_info)
                ordered_info_list = sorted(filtered_info_list, key=lambda x: getattr(x, order_name))
            else:
                ordered_info_list = sorted(self.name_info, key=lambda x: getattr(x, order_name))

            return ordered_info_list
        raise LookupError(f"Unable to find attribute {order_name} in NameInfo")
    

    def get_ordered_linked_info(self, list_order: Literal["partition","name"] = "partition", order_name: str = "") -> list[tuple[PartitionInfo,NameInfo]]:
        linked_info: list[tuple[PartitionInfo,NameInfo]] = []
        partition_info = self.get_ordered_partition_info('hash', 'dataSize')
        name_info = self.get_ordered_name_info('partitionOffset')

        for i in range(len(partition_info)):
            linked_info.append((partition_info[i], name_info[i]))

        if list_order == "partition" and order_name in PartitionInfo.__dataclass_fields__.keys():
            ordered_linked_info = sorted(linked_info, key=lambda x: getattr(x[0], order_name))
        elif list_order == "name" and order_name in NameInfo.__dataclass_fields__.keys():
            ordered_linked_info = sorted(linked_info, key=lambda x: getattr(x[1], order_name))
        else:
            raise LookupError(f"Unable to find attribute {order_name} in either PartitionInfo or NameInfo")
        return ordered_linked_info


def get_class_by_magic(magic: bytes, file_type: int, filename: str = "") -> type[PataponDataClass]:
    param_magic = GenericParamHeader.__dataclass_fields__['magic'].default
    gxx_magic = GxxHeader.__dataclass_fields__['magic'].default
    gxt_magic = GXTHeader.__dataclass_fields__['magic'].default
    bnd_magic = BNDHeader.__dataclass_fields__['magic'].default
    effect2_magic = EffectKeyHeader.__dataclass_fields__['magic'].default

    if magic.startswith(bnd_magic):
        if file_type == 1:
            cls = BND
        else:
            cls = BNS
    elif magic.startswith(gxx_magic):
        cls = Gxx
    elif magic.startswith(gxt_magic):
        cls = GXT
    elif magic.startswith(effect2_magic):
        cls = EffectKey
    else:
        temp_cls, cls_type = param.get_dataclass_from_filename(filename)
        if temp_cls is not None:
            if (magic.startswith(param_magic) and cls_type == 1) or cls_type == 2:
                cls = temp_cls
            else:
                cls = UnknownDataClass
        else:
            cls = UnknownDataClass
    return cls


@dataclass
class BND(PataponDynamicDataClass):
    header: BNDHeader = field(default_factory=BNDHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    partitions: list[PataponDataClass] = field(default_factory=list[PataponDataClass], metadata={"meta": FieldMetadata("bnd_files", 1), "tags": [FieldTag("file", "body")]})


    def process(self, data: PataponDataIO, file_offset: int = 0, section_size: int = -1) -> tuple[int,list[PataponDataClass]]:
        linked_info = self.header.get_ordered_linked_info('partition', 'dataOffset')

        new_value: list[PataponDataClass] = []

        offset = 0
        for info in linked_info:
            cls: type[PataponDataClass]

            partition_info = info[0]
            filename = info[1].name.strip("\x00")

            # extract the magic bit from the file, if it exists
            magic = data.read(file_offset+offset, 0x10)
            
            # get the filetype (only applicable to BND and BNS)
            filetype = int.from_bytes(data.read(file_offset+offset+4, 4), 'little')

            # get the class to use for data extraction
            cls = get_class_by_magic(magic, filetype, filename)
            size = partition_info.dataSize
            try:
                new_value.append(cls.from_bytes(data, file_offset=file_offset+offset, section_size=size))
            except:
                print(f"issue with processing file {filename}")
                new_value.append(UnknownDataClass.from_bytes(data, file_offset=file_offset+offset, section_size=size))
            
            alignment = self.header.alignSize
            offset += size
            if offset % alignment != 0:
                offset += alignment - (size % alignment)

        return offset, new_value



# BNS
@dataclass
class BNSPartitionInfo(PataponStaticDataClass, PataponDataClassElement):
    partition_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    partition_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2, count=2)})


@dataclass
class BNSHeader(PataponDynamicDataClass, PataponDataClassHeader):
    magic: bytes = field(default=b"BND", metadata={"meta": FieldMetadata("bytes", 0, size=0x4)})
    flag: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    alignSize: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("alignment", "source")]})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3, count=2)})
    dataTableOffset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4), "tags": [FieldTag("dataTableOffset", "source")]})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    nFiles: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6), "tags": [FieldTag("file_count", "source")]})
    nPartitionInfo: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("partition_info_count", "source")]})
    partition_info: list[BNSPartitionInfo] = field(default_factory=list[BNSPartitionInfo], metadata={"meta": FieldMetadata("dataclass", 8), "tags": [FieldTag("partition_info_count", "count")]})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 9, count=2)})



@dataclass
class BNS(PataponDynamicDataClass):
    header: BNSHeader = field(default_factory=BNSHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    partitions: list[PataponDataClass] = field(default_factory=list[PataponDataClass], metadata={"meta": FieldMetadata("bnd_files", 1), "tags": [FieldTag("file", "body")]})


    def process(self, data: PataponDataIO, file_offset: int = 0, section_size: int = -1) -> tuple[int,list[PataponDataClass]]:
        partition_info = self.header.partition_info

        new_value: list[PataponDataClass] = []

        offset = 0
        for info in partition_info:
            cls: type[PataponDataClass]

            # grab the first 0x10 bytes from the file to check for magic
            magic = data.read(file_offset+offset, 0x10)

            # get the filetype (only applicable to BND and BNS)
            filetype = int.from_bytes(data.read(file_offset+offset+4, 4), 'little')

            # get the class to use for data extraction
            cls = get_class_by_magic(magic, filetype)
            size = info.partition_size
            try:
                new_value.append(cls.from_bytes(data, file_offset=file_offset+offset, section_size=size))
            except:
                print(f"issue with processing file at {hex(info.offset)}")
                new_value.append(UnknownDataClass.from_bytes(data, file_offset=file_offset+offset, section_size=size))
            
            alignment = self.header.alignSize
            offset += size
            if offset % alignment != 0:
                offset += alignment - (size % alignment)

        return offset, new_value