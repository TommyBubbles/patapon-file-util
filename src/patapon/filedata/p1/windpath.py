from dataclasses import field, dataclass
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponDataClassElement,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    FieldMetadata,
    FieldTag
)



@dataclass
class WindPathInfo(PataponStaticDataClass, PataponDataClassElement):
    nodeIndex: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    numNode: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("node_count", "source")]})
    nodeArray: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    length: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    name: str = field(default="", metadata={"meta": FieldMetadata("string", 4, size=0x20)})


@dataclass
class WindPathHeader(PataponDataClassHeader, PataponStaticDataClass):
    magic: bytes = field(default=b"Path", metadata={"meta": FieldMetadata("bytes", 0, size=0x4)})
    isEndianRevers: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int8", 2, count=3)})
    numPath: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("path_count", "source")]})
    pathArray: list[WindPathInfo] = field(default_factory=list[WindPathInfo], metadata={"meta": FieldMetadata("dataclass", 4), "tags": [FieldTag("path_count", "count"), FieldTag("path_array", "source")]})
    padding: int = field(default=0, metadata={"meta": FieldMetadata("signed_int", 5)})



@dataclass
class WindPathVector(PataponStaticDataClass, PataponDataClassBody):
    x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
    y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
    z: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    w: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})


@dataclass
class WindPathNode(PataponStaticDataClass, PataponDataClassElement):
    pos: WindPathVector = field(default_factory=WindPathVector, metadata={"meta": FieldMetadata("dataclass", 0)})
    inVec: WindPathVector = field(default_factory=WindPathVector, metadata={"meta": FieldMetadata("dataclass", 1)})
    outVec: WindPathVector = field(default_factory=WindPathVector, metadata={"meta": FieldMetadata("dataclass", 2)})
    length: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 4, count=3)})



@dataclass
class WindPathNodeList(PataponDynamicDataClass, PataponDataClassElement):
    windpath_nodes: list[WindPathNode] = field(default_factory=list[WindPathNode], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("path_array", "count", 0, FieldTag("node_count", "source"))]})


@dataclass
class WindPath(PataponDynamicDataClass):
    header: WindPathHeader = field(default_factory=WindPathHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    windpaths: WindPathNodeList = field(default_factory=WindPathNodeList, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})