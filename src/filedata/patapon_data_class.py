from struct import pack, unpack
from dataclasses import dataclass
from typing import Any

fieldmeta = dict[str, Any]

@dataclass
class PataponDataClass:
    byte_order = "<"

    def __init__(self):
        pass


    @classmethod
    def from_bytes(cls, raw: bytes):
        new_inst = cls()
        raw_values = unpack(cls.format_string(), raw)
        pos_list = cls._field_starts()

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            pos = pos_list[metadata["pos"]]

            if metadata["type"] == "s":
                encoding = metadata.get("encoding", "utf-8")
                new_value = bytes(raw_values[pos]).decode(encoding)
            elif metadata["type"] == "i":
                values = metadata.get("values", -1)

                # only really used for filler at this point
                if values != -1:
                    new_value = []
                    for i in range(0, metadata["values"]):
                        new_value.append(raw_values[pos+i])
                else:
                    new_value = raw_values[pos]
            else:
                new_value = raw_values[pos]
            setattr(new_inst, name, new_value)
        return new_inst
            
            
    @classmethod
    def format_string(cls) -> str:
        format_list = list("" for _ in cls.__dataclass_fields__.values())
        
        for field in cls.__dataclass_fields__.values():
            metadata: fieldmeta = field.metadata
            field_type = metadata["type"]
            if field_type == 's':
                field_amount = metadata["size"]
            elif field_type == 'i':
                field_amount = metadata.get("values", "")
            else:
                field_amount = ""
            format_list[metadata["pos"]] = f"{field_amount}{field_type}"
        
        return cls.byte_order + "".join(format_list)


    @classmethod
    def _field_starts(cls) -> list[int]:
        size_list = list(0 for _ in cls.__dataclass_fields__.values())

        for field in cls.__dataclass_fields__.values():
            metadata: fieldmeta = field.metadata
            field_type = metadata["type"]
            if field_type == 's':
                field_size = 1
            elif field_type == 'i':
                field_size = metadata.get("values", 1)
            else:
                field_size = 1
            size_list[metadata["pos"]] = field_size
        
        pos_list = [0]
        for i in range(1, len(size_list)):
            pos_list.append(pos_list[i-1] + size_list[i-1])
        
        return pos_list
    
    @classmethod
    def verify_filler(cls, obj: 'PataponDataClass') -> bool:
        zeroflag = True
        for field in cls.__dataclass_fields__.keys():
            if field.startswith('filler'):
                for val in getattr(obj, field):
                    if val != 0:
                        print(f"non-zero value found in {field}: {val}")
                        zeroflag = False
        return zeroflag