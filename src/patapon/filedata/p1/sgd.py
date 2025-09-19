# TODO: figure out how to make this dataclass work with existing tagging system
from dataclasses import dataclass, field
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassElement,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    FieldMetadata,
    FieldTag
)

@dataclass
class SGDHeader(PataponStaticDataClass, PataponDataClassHeader):
    magic: bytes = field(default=b"SEQD", metadata={"meta": FieldMetadata("bytes", 0, size=4)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    data_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    data_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})



@dataclass
class SGDRGNDInfo(PataponStaticDataClass, PataponDataClassElement):
    data: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 0, size=0x38)})


@dataclass
class SGDRGNDSection(PataponDynamicDataClass):
    magic: bytes = field(default=b"SEQD", metadata={"meta": FieldMetadata("bytes", 0, size=4)})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    rgnd_info_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    rgnd_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    sequence_info: list[SGDRGNDInfo] = field(default_factory=list[SGDRGNDInfo], metadata={"meta": FieldMetadata("dataclass", 6), "tags": [FieldTag("sequence_count", "count")]})



@dataclass
class SGDSequenceInfo(PataponStaticDataClass, PataponDataClassElement):
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    bytes_1: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 2, size=0x24)})
    

@dataclass
class SGDSequenceSection(PataponDynamicDataClass):
    magic: bytes = field(default=b"SEQD", metadata={"meta": FieldMetadata("bytes", 0, size=4)})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    sequence_info_section_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    sequence_info_section_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    sequence_info_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6), "tags": [FieldTag("sequence_count", "source")]})
    sequence_info_offsets: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("sequence_count", "count")]})
    sequence_info: list[SGDSequenceInfo] = field(default_factory=list[SGDSequenceInfo], metadata={"meta": FieldMetadata("dataclass", 8), "tags": [FieldTag("sequence_count", "count")]})



@dataclass
class SGDWaveInfo(PataponStaticDataClass, PataponDataClassElement):
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    file_format: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 2)})
    channel_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 3)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 4)})
    frequency: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    filler_3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6, count=2)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 7)})
    i2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 8)})
    filler_2: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    total_samples: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    i3: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 11)})
    i4: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 12)})
    audio_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 13), "tags": [FieldTag("data_size", "source")]})
    audio_start: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 14)})
    audio_end: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 15)})


@dataclass
class SGDWaveSection(PataponDynamicDataClass):
    magic: bytes = field(default=b"WAVE", metadata={"meta": FieldMetadata("bytes", 0, size=4)})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    wave_info_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("wave_info_count", "source")]})
    wave_info: list[SGDWaveInfo] = field(default_factory=list[SGDWaveInfo], metadata={"meta": FieldMetadata("string", 4), "tags": [FieldTag("wave_info_count", "count"), FieldTag("wave_info", "source")]})



@dataclass
class SGDNameInfo(PataponStaticDataClass, PataponDataClassElement):
    index: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 0)})
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int16", 1)})
    name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})


@dataclass
class SGDNameSection(PataponDynamicDataClass):
    magic: bytes = field(default=b"NAME", metadata={"meta": FieldMetadata("bytes", 0, size=4)})
    size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    name_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("name_count", "source")]})
    name_info_list: list[SGDNameInfo] = field(default_factory=list[SGDNameInfo], metadata={"meta": FieldMetadata("dataclass", 4), "tags": [FieldTag("name_count", "count")]})
    name_list: list[str] = field(default_factory=list[str], metadata={"meta": FieldMetadata("string", 5), "tags": [FieldTag("name_count", "count")]})



@dataclass
class SGDCompressedAudioSampleFrame(PataponStaticDataClass, PataponDataClassElement):
    filter_shift: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 0, size=1)})
    flags: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 1, size=1)})
    data: bytes = field(default=b"", metadata={"meta": FieldMetadata("bytes", 2, size=14)})


    @property
    def filter(self) -> int:
        return (self.filter_shift >> 4) & 0xf

    @property
    def shift(self) -> int:
        return self.filter_shift & 0xf


@dataclass
class SGDCompressedAudio(PataponDynamicDataClass, PataponDataClassElement):
    pass



@dataclass
class SGDDataSection(PataponDynamicDataClass):
    audio_data: list[SGDCompressedAudio] = field(default_factory=list[SGDCompressedAudio], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("wave_info_count", "count")]})



@dataclass
class SGD(PataponDynamicDataClass):
    header: SGDHeader = field(default_factory=SGDHeader, metadata={"meta": FieldMetadata("dataclass", 0)})
    rgnd_section: SGDRGNDSection = field(default_factory=SGDRGNDSection, metadata={"meta": FieldMetadata("dataclass", 1)})
    sequence_section: SGDSequenceSection = field(default_factory=SGDSequenceSection, metadata={"meta": FieldMetadata("dataclass", 2)})
    wave_section: SGDWaveSection = field(default_factory=SGDWaveSection, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("data_header", "header")]})
    name_section: SGDNameSection = field(default_factory=SGDNameSection, metadata={"meta": FieldMetadata("dataclass", 4)})
    data_section: SGDDataSection = field(default_factory=SGDDataSection, metadata={"meta": FieldMetadata("dataclass", 5), "tags": [FieldTag("data_header", "body")]})
