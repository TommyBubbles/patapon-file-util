from struct import pack, unpack
from dataclasses import dataclass, field
from typing import Any 
from .patapon_data_class import PataponDataClass

@dataclass
class EquipParam(PataponDataClass):
    byte_order = "<"
    iname: str = field(metadata={"pos": 0, "type": "s", "size": 0x20, "encoding": "utf-8"})
    id: int = field(metadata={"pos": 1, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 4})
    i1: int = field(metadata={"pos": 3, "type": "i"})
    i2: int = field(metadata={"pos": 4, "type": "i"})
    filler_2: list[int] = field(metadata={"pos": 5, "type": "i", "values": 1})
    i3: int = field(metadata={"pos": 6, "type": "i"})
    filler_3: list[int] = field(metadata={"pos": 7, "type": "i", "values": 2})
    i4: int = field(metadata={"pos": 8, "type": "i"})
    filler_4: list[int] = field(metadata={"pos": 9, "type": "i", "values": 20})
    mname: str = field(metadata={"pos": 10, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_5: list[int] = field(metadata={"pos": 11, "type": "i", "values": 8})


    def __init__(self):
        pass