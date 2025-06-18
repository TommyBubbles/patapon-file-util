from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass

@dataclass
class CollisionParam(PataponStaticDataClass):
    file_name: str = field(metadata={"pos": 0, "type": "s", "size": 0x20, "encoding": "utf-8"})
    i1: int = field(metadata={"pos": 1, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 2, "type": "i", "values": 3})
    f1: float = field(metadata={"pos": 3, "type": "f"})
    f2: float = field(metadata={"pos": 4, "type": "f"})
    filler_2: list[int] = field(metadata={"pos": 5, "type": "i", "values": 1})
    type: str = field(metadata={"pos": 6, "type": "s", "size": 0x20, "encoding": "utf-8"})
    i2: int = field(metadata={"pos": 7, "type": "i"})
    s1: str = field(metadata={"pos": 8, "type": "s", "size": 0x20, "encoding": "utf-8"})


    def __init__(self):
        super().__init__()