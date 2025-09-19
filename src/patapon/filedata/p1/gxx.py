from dataclasses import field, dataclass
from ..patapon_data_class import (
    PataponDataClassHeader,
    PataponDataClassBody,
    PataponDataClassElement,
    PataponDataClass,
    PataponStaticDataClass,
    PataponDynamicDataClass,
    FieldMetadata,
    FieldTag
)



@dataclass
class GxxHeader(PataponStaticDataClass):
    """
    Main Header for Gxx Files
    Basic Breakdown:
        - starts with magic to determine the type of file it is
        - TBD (seems to suggest an offset of some kind)
        - pointers to and sizes of four different sections of information listed
          in reverse order than they are stored physically on the file
            1. Mesh Information
            2. Motion Command Information
            3. Vertex Information
            4. Unknown (empty space?)
    """
    magic: bytes = field(default=b"XXG.01.0OMG.", metadata={"meta": FieldMetadata("bytes", 0, size=0x10, encoding="utf-8")})
    offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=3)})
    mesh_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    mesh_info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4), "tags": [FieldTag("mesh_info_size", "source")]})
    motion_commands_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5)})
    motion_commands_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6), "tags": [FieldTag("motion_commands_size", "source")]})
    vertex_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    vertex_info_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 8), "tags": [FieldTag("vertex_info_size", "source")]})
    unknown_1_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    unknown_1_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})



def difference(first: int, second: int) -> int:
    return first - second



@dataclass
class GxSectionHeader(PataponStaticDataClass, PataponDataClassHeader):
    id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    used_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("used_size", "source")]})
    total_size: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("total_size", "source")]})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 3, count=13)})



# Vertex Information
# @dataclass
# class GxxVertexInfo(PataponStaticDataClass, PataponDataClassElement):
#     uv_x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 0)})
#     uv_y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 1)})
#     color: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 2, size=4)})
#     pos_x: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 3)})
#     pos_y: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 4)})
#     pos_z: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 5)})


@dataclass
class GxxVertexInfoSection(PataponDynamicDataClass, PataponDataClassBody):
    # vertex_info: list[GxxVertexInfo] = field(default_factory=list[GxxVertexInfo], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("used_size", "byte_size")]})
    vertex_info_bytes: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 0), "tags": [FieldTag("used_size", "size")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 1), "tags": [FieldTag("unk1_padding", "size", func=difference, func_params={"first": "total_size", "second": "used_size"})]})


@dataclass
class GxxVertexSectionElement(PataponDynamicDataClass, PataponDataClassElement):
    header: GxSectionHeader = field(default_factory=GxSectionHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("command_section", "header")]})
    body: GxxVertexInfoSection = field(default_factory=GxxVertexInfoSection, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("command_section", "body")]})


@dataclass
class GxxVertexSection(PataponDynamicDataClass, PataponDataClassBody):
    vertex_info: list[GxxVertexSectionElement] = field(default_factory=list[GxxVertexSectionElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("vertex_info_size", "byte_size")]})



# Motion Command Information
@dataclass
class GxxMotionCommand(PataponStaticDataClass, PataponDataClassElement):
    value: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 0, size=3)})
    command_id: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int8", 1)})


@dataclass
class GxxMotionCommandSection(PataponDynamicDataClass, PataponDataClassBody):
    commands: list[GxxMotionCommand] = field(default_factory=list[GxxMotionCommand], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("used_size", "byte_size")]})
    padding_1: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 1), "tags": [FieldTag("unk1_padding", "size", func=difference, func_params={"first": "total_size", "second": "used_size"})]})


@dataclass
class GxxMotionCommandElement(PataponDynamicDataClass, PataponDataClassElement):
    header: GxSectionHeader = field(default_factory=GxSectionHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("command_section", "header")]})
    body: GxxMotionCommandSection = field(default_factory=GxxMotionCommandSection, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("command_section", "body")]})


@dataclass
class GxxMotionCommandList(PataponDynamicDataClass, PataponDataClassBody):
    command_sections: list[GxxMotionCommandElement] = field(default_factory=list[GxxMotionCommandElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("motion_commands_size", "byte_size")]})


# Mesh Information
@dataclass
class GxxMeshHeader(PataponStaticDataClass, PataponDataClassHeader):
    num_element: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    texture_pointers_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 2)})
    texture_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3), "tags": [FieldTag("texture_count", "source")]})
    motion_info_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    motion_info_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 5), "tags": [FieldTag("motion_info_count", "source")]})
    bone_names_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    bone_names_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7), "tags": [FieldTag("bone_names_count", "source")]})
    top_bounds: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 8, count=3)})
    bottom_bounds: list[float] = field(default_factory=list[float], metadata={"meta": FieldMetadata("float", 9, count=3)})



# Texture Pointers
@dataclass
class GxxTexturePointerInfo(PataponDynamicDataClass, PataponDataClassBody):
    texture_pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("texture_count", "count")]})



# Motion Info
def func_motion_frame_count(count: int) -> int:
    if count == 1:
        return 0
    return count


@dataclass
class GxxMotionInfoElement(PataponDynamicDataClass, PataponDataClassElement):
    motion_frame_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    motion_frame_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    motion_framerate: float = field(default=0.0, metadata={"meta": FieldMetadata("float", 2)})
    motion_loops: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})


@dataclass
class GxxMotionInfoTable(PataponDynamicDataClass, PataponDataClassBody):
    motion_infos: list[GxxMotionInfoElement] = field(default_factory=list[GxxMotionInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("motion_info_count", "count")]})
    motion_pointer_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1), "tags": [FieldTag("motion_count", "source")]})
    motion_pointers: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2), "tags": [FieldTag("motion_count", "count")]})



# Bone Name
def get_bone_name_padding(bone_names: list[str]):
    alignment = 0x10
    if bone_names is None or len(bone_names) == 0:
        return alignment

    cur_size = 0
    for name in bone_names:
        cur_size += len(name)
    if cur_size % 4 == 0:
        return alignment - 4
    return alignment - (cur_size % 4)


@dataclass
class GxxBoneNameInfoElement(PataponStaticDataClass, PataponDataClassElement):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    name_pointers: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})


@dataclass
class GxxBoneName(PataponDynamicDataClass, PataponDataClassBody):
    name_pointers: list[GxxBoneNameInfoElement] = field(default_factory=list[GxxBoneNameInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("bone_names_count", "count")]})
    names: list[str] = field(default_factory=list[str], metadata={"meta": FieldMetadata("string", 1), "tags": [FieldTag("bone_names_count", "count"), FieldTag("bone_names", "source")]})
    padding: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 2), "tags": [FieldTag("padding", "size", func=get_bone_name_padding, func_params={"bone_names": "bone_names"})]})



# texture info
@dataclass
class GxxTextureInfoElement(PataponStaticDataClass, PataponDataClassElement):
    i1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0)})
    file_name_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})
    filler_1: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 2, count=2)})
    offset_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 3)})
    count_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 4)})
    filler_2: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 5, count=2)})
    motion_pointers_offset: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 6)})
    motion_pointers_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 7)})
    filler_3: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 8, count=2)})
    i6: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 9)})
    motion_pointer: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 10)})
    file_name: str = field(default="", metadata={"meta": FieldMetadata("string", 11, size=0x10, encoding="utf-8")})
    filler_4: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 12, count=2)})


@dataclass
class GxxTextureInfo(PataponDynamicDataClass, PataponDataClassBody):
    info_list: list[GxxTextureInfoElement] = field(default_factory=list[GxxTextureInfoElement], metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("texture_count", "count")]})



def get_mesh_section_padding(size: int, obj: PataponDataClass) -> int:
    return size - obj.get_byte_size(0, 5)


@dataclass
class GxxMeshSection(PataponDynamicDataClass, PataponDataClassBody):
    mesh_header: GxxMeshHeader = field(default_factory=GxxMeshHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("mesh", "header")]})
    texture_pointers: GxxTexturePointerInfo = field(default_factory=GxxTexturePointerInfo, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("mesh", "body")]})
    motion_info_table: GxxMotionInfoTable = field(default_factory=GxxMotionInfoTable, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("mesh", "body")]})
    bone_names: GxxBoneName = field(default_factory=GxxBoneName, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("mesh", "body")]})
    texture_list: GxxTextureInfo = field(default_factory=GxxTextureInfo, metadata={"meta": FieldMetadata("dataclass", 4), "tags": [FieldTag("mesh", "body")]})
    padding: bytes = field(default=b'', metadata={"meta": FieldMetadata("padding", 5), "tags": [FieldTag("padding_size", "size", func=get_mesh_section_padding, func_params={"size": "mesh_info_size", "obj": "self"})]})



# Base Gxx class
@dataclass
class Gxx(PataponDynamicDataClass):
    header: GxxHeader = field(default_factory=GxxHeader, metadata={"meta": FieldMetadata("dataclass", 0), "tags": [FieldTag("file", "header")]})
    vertex_section: GxxVertexSection = field(default_factory=GxxVertexSection, metadata={"meta": FieldMetadata("dataclass", 1), "tags": [FieldTag("file", "body")]})
    motion_commands_section: GxxMotionCommandList = field(default_factory=GxxMotionCommandList, metadata={"meta": FieldMetadata("dataclass", 2), "tags": [FieldTag("file", "body")]})
    mesh_section: GxxMeshSection = field(default_factory=GxxMeshSection, metadata={"meta": FieldMetadata("dataclass", 3), "tags": [FieldTag("file", "body")]})
