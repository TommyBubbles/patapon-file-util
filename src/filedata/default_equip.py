from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass

@dataclass
class DefaultEquip(PataponStaticDataClass):
    file_name: str = field(metadata={"pos": 0, "type": "s", "size": 0x20, "encoding": "utf-8"})
    i1: int = field(metadata={"pos": 1, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 4})
    i2: int = field(metadata={"pos": 3, "type": "i"})
    filler_2: list[int] = field(metadata={"pos": 4, "type": "i", "values": 2})
    s1: str = field(metadata={"pos": 5, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s2: str = field(metadata={"pos": 6, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s3: str = field(metadata={"pos": 7, "type": "s", "size": 0x20, "encoding": "utf-8"})
    model_name: str = field(metadata={"pos": 8, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s4: str = field(metadata={"pos": 9, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s5: str = field(metadata={"pos": 10, "type": "s", "size": 0x20, "encoding": "utf-8"})


    def __init__(self):
        super().__init__()