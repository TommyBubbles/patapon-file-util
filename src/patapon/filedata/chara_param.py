from dataclasses import dataclass, field 
from .patapon_data_class import PataponStaticDataClass

@dataclass
class CharaParam(PataponStaticDataClass):
    internal_name: str = field(metadata={"pos": 0, "type": "s", "size": 0x20, "encoding": "utf-8"})
    internal_id: int = field(metadata={"pos": 1, "type": "i"})
    i1: int = field(metadata={"pos": 2, "type": "i"})
    position_id_1: int = field(metadata={"pos": 3, "type": "i"})
    type_1: int = field(metadata={"pos": 4, "type": "i"})
    position_id_2: int = field(metadata={"pos": 5, "type": "i"})
    f1: float = field(metadata={"pos": 6, "type": "f"})
    type_2: int = field(metadata={"pos": 7, "type": "i"})
    position_id_3: int = field(metadata={"pos": 8, "type": "i"})
    filler_1: list[int] = field(metadata={"pos": 9, "type": "i", "values": 0x21})
    f2: float = field(metadata={"pos": 10, "type": "f"})
    filler_2: list[int] = field(metadata={"pos": 11, "type": "i", "values": 0x2})
    big: int = field(metadata={"pos": 12, "type": "i"})
    i2: int = field(metadata={"pos": 13, "type": "i"})
    flying: int = field(metadata={"pos": 14, "type": "i"})
    filler_3: list[int] = field(metadata={"pos": 15, "type": "i", "values": 0x1})
    s1: str = field(metadata={"pos": 16, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_4: list[int] = field(metadata={"pos": 17, "type": "i", "values": 0x10})
    model_internal_name: str = field(metadata={"pos": 18, "type": "s", "size": 0x20, "encoding": "utf-8"})
    class_data_file: str = field(metadata={"pos": 19, "type": "s", "size": 0x20, "encoding": "utf-8"})
    japenese_name: str = field(metadata={"pos": 20, "type": "s", "size": 0x20, "encoding": "shift-jis"})
    default_weapon: str = field(metadata={"pos": 21, "type": "s", "size": 0x20, "encoding": "utf-8"})
    hero_mode_icon: str = field(metadata={"pos": 22, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s2: str = field(metadata={"pos": 23, "type": "s", "size": 0x20, "encoding": "utf-8"})
    s3: str = field(metadata={"pos": 24, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_5: list[int] = field(metadata={"pos": 25, "type": "i", "values": 0x8})
    s4: str = field(metadata={"pos": 26, "type": "s", "size": 0x20, "encoding": "utf-8"})
    filler_6: list[int] = field(metadata={"pos": 27, "type": "i", "values": 0x18})


    def __init__(self):
        super().__init__()