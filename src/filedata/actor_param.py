from dataclasses import dataclass, field 
from .patapon_data_class import PataponDataClass

@dataclass
class ActorParam(PataponDataClass):
    byte_order = "<"
    file_id: str = field(metadata={"pos": 0, "type": "s", "size": 0x20, "encoding": "utf-8"})
    i1: int = field(metadata={"pos": 1, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 3})
    str1: str = field(metadata={"pos": 3, "type": "s", "size": 0x10, "encoding": "utf-8"})
    i2: int = field(metadata={"pos": 4, "type": "i"})
    filler_2: list[int] = field(metadata={"pos": 5, "type": "i", "values": 7})
    str2: str = field(metadata={"pos": 6, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str3: str = field(metadata={"pos": 7, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str4: str = field(metadata={"pos": 8, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str5: str = field(metadata={"pos": 9, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str6: str = field(metadata={"pos": 10, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str7: str = field(metadata={"pos": 11, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_3: list[int] = field(metadata={"pos": 12, "type": "i", "values": 24})
    str8: str = field(metadata={"pos": 13, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str9: str = field(metadata={"pos": 14, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str10: str = field(metadata={"pos": 15, "type": "s", "size": 0x20, "encoding": "utf-8"})
    str11: str = field(metadata={"pos": 16, "type": "s", "size": 0x20, "encoding": "utf-8"})


    def __init__(self):
        super().__init__()