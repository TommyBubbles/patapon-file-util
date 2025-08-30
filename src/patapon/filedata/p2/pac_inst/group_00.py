from dataclasses import dataclass, field
from patapon.filedata.patapon_data_class import FieldMetadata, PataponStaticDataClass, PataponDataClassElement, FieldTag

class PacInstruction(PataponDataClassElement):
    id: bytes
    _name: str


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val


@dataclass
class PacInstruction00_0001(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x01\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_end"
        return instance


@dataclass
class PacInstruction00_0002(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x02\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    jump_address: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1)})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_jmp"
        return instance
    

@dataclass
class PacInstruction00_0003(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x03\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    jump_address: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1)})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_call"
        return instance
    

@dataclass
class PacInstruction00_0004(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x04\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    value_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("value_flag", "source")]})
    value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("value_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_result"
        return instance


@dataclass
class PacInstruction00_0005(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x05\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    compare_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("compare_flag", "source")]})
    compare_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("compare_flag", "type")]})
    jump_address: int = field(default=0, metadata={"metadata": FieldMetadata('unsigned_int', 3)})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_resJmp"
        return instance
    

@dataclass
class PacInstruction00_0006(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x06\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    compare_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("compare_flag", "source")]})
    compare_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("compare_flag", "type")]})
    jump_address: int = field(default=0, metadata={"metadata": FieldMetadata('unsigned_int', 3)})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_resCall"
        return instance
    

@dataclass
class PacInstruction00_0007(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x07\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    source_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 3), "tags": [FieldTag("source_flag", "source")]})
    source_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 4), "tags": [FieldTag("source_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_mov"
        return instance
    

@dataclass
class PacInstruction00_0008(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x08\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    addition_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 3), "tags": [FieldTag("addition_flag", "source")]})
    addition_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 4), "tags": [FieldTag("addition_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_add"
        return instance
    

@dataclass
class PacInstruction00_0009(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x09\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    subtraction_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 3), "tags": [FieldTag("subtraction_flag", "source")]})
    subtraction_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 4), "tags": [FieldTag("subtraction_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_sub"
        return instance
    

@dataclass
class PacInstruction00_000A(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0A\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    multiplcation_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 3), "tags": [FieldTag("multiplcation_flag", "source")]})
    multiplcation_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 4), "tags": [FieldTag("multiplcation_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_mul"
        return instance
    

@dataclass
class PacInstruction00_000B(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0B\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    division_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 3), "tags": [FieldTag("division_flag", "source")]})
    division_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 4), "tags": [FieldTag("division_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_div"
        return instance
    

@dataclass
class PacInstruction00_000C(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0C\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_inc"
        return instance
    

@dataclass
class PacInstruction00_000D(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0D\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_dec"
        return instance
    

@dataclass
class PacInstruction00_000E(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0E\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    destination_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("destination_flag", "source")]})
    destination_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("destination_flag", "type")]})
    jump_address: int = field(default=0, metadata={"metadata": FieldMetadata('unsigned_int', 3)})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_loop"
        return instance
    

@dataclass
class PacInstruction00_000F(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x0F\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    waiting_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("waiting_flag", "source")]})
    waiting_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("waiting_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_waitFrame"
        return instance
    

@dataclass
class PacInstruction00_0010(PataponStaticDataClass, PacInstruction):
    id: bytes = field(default=b'\x25\x00\x10\x00', metadata={"meta": FieldMetadata('bytes', 0, size=4, byte_order=">")}, init=False)
    source_flag: int = field(default=0, metadata={"meta": FieldMetadata('unsigned_int', 1), "tags": [FieldTag("source_flag", "source")]})
    source_value: int | float = field(default=0, metadata={"metadata": FieldMetadata('arg_pair_value', 2), "tags": [FieldTag("source_flag", "type")]})


    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        instance.name = "cmd_waitTime"
        return instance