from struct import pack, unpack, calcsize
from dataclasses import dataclass, Field, field
from typing import Any, Callable

fieldmeta = dict[str, Any]


class PataponDataClassHeader:
    _start_pos: int


    def __init__(self):
        pass


    @property
    def start_pos(self) -> int:
        return self._start_pos
    
    @start_pos.setter
    def start_pos(self, value: int):
        self._start_pos = value


class PataponDataClassBody:
    byte_order: str = ">"
    _start_pos: int
    _header: PataponDataClassHeader


    def __init__(self):
        pass

    
    @property
    def start_pos(self) -> int:
        return self._start_pos
    
    @start_pos.setter
    def start_pos(self, value: int):
        self._start_pos = value


    @property
    def header(self) -> PataponDataClassHeader:
        return self._header
    
    @header.setter
    def header(self, value: PataponDataClassHeader):
        self._header = value


@dataclass
class PataponDataClass:
    @classmethod
    def from_bytes(cls, raw: bytes, *, header: PataponDataClassHeader | None = ...) -> 'PataponDataClass': ...
    def to_bytes(self) -> bytes: ...
    @classmethod
    def format_string(cls) -> str: ...
    def get_byte_size(self) -> int: ...


    def __init__(self):
        pass


    @classmethod
    def find_name_by_tag(cls, tag: str, *_, type_search: str = "", exclude: str = "") -> list[str]:
        results = []

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            if metadata.get("tag", "") == tag and \
               (type_search == "" or metadata["type"] == type_search) and \
               name != exclude:
                results.append(name)
        
        return results
    

    @classmethod
    def find_value_by_tag(cls, obj: 'PataponDataClass', tag: str) -> Any | None:
        fields = obj.find_name_by_tag(tag)
        if len(fields) == 1:
            field_value = getattr(obj, fields[0])
        elif len(fields) > 1:
            raise LookupError(f'Too many fields in {obj} with the same tag: {fields}')
        else:
            field_value = None
        return field_value


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
    

    @classmethod
    def verify_datafield_pos(cls):
        field_list: list[tuple] = list(() for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            field_list[metadata["pos"]].append(name)

        valid = True
        for i in range(len(field_list)):
            item: tuple = field_list[i]
            if len(item) == 0:
                print(f"no fields found at position {i}")
                valid = False
            elif len(item) >= 2:
                print(f"too many fields found at position {i}: {item}")
                valid = True

        return valid


class PataponStaticDataClass(PataponDataClass):
    byte_order: str = "<"
    @classmethod
    def from_bytes(cls, raw: bytes, *_, header: PataponDataClassHeader | None = None) -> 'PataponStaticDataClass':
        new_inst = cls()
        format_string = cls.format_string()

        # base case for empty header/body
        if calcsize(format_string) == 0:
            return new_inst

        raw_values = unpack(format_string, raw)
        pos_list = cls._field_starts()

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            pos = pos_list[metadata["pos"]]

            if metadata["type"] == "s":
                encoding = metadata.get("encoding", "utf-8")
                new_value = bytes(raw_values[pos]).decode(encoding)
            elif metadata["type"] in ['I', 'i', 'f']:
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
    

    def to_bytes(self) -> bytes:
        cls = self.__class__
        pos_list: list[int] = cls._field_starts()
        values = list(b"" for _ in range(cls._pack_size()))

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            
            pos: int = pos_list[metadata["pos"]]
            value = getattr(self, name)

            if metadata["type"] == "s":
                values[pos] = str(value).encode(metadata["encoding"])
            elif metadata["type"] in ['I', 'i', 'f']:
                filler_values = metadata.get("values", -1)

                # only really used for filler at this point
                if filler_values != -1:
                    for i in range(0, metadata["values"]):
                        values[pos+i] = list(value)[i]
                else:
                    values[pos] = value
            else:
                values[pos] = value

        return pack(cls.format_string(), *values)
            
            
    @classmethod
    def format_string(cls) -> str:
        format_list = list("" for _ in cls.__dataclass_fields__.values())
        
        for field in cls.__dataclass_fields__.values():
            metadata: fieldmeta = field.metadata
            field_type = metadata["type"]
            if field_type == 's':
                field_amount = metadata["size"]
            elif field_type in ['I', 'i', 'f']:
                field_amount = metadata.get("values", "")
            else:
                field_amount = ""
            format_list[metadata["pos"]] = f"{field_amount}{field_type}"
        
        return cls.byte_order + "".join(format_list)


    @classmethod
    def _field_starts(cls) -> list[int]:
        """
        only used with from_bytes and to_bytes
        returns the starting position of each field as it
        would appear in the struct unpack return value
        """
        size_list = list(0 for _ in cls.__dataclass_fields__.values())

        for field in cls.__dataclass_fields__.values():
            metadata: fieldmeta = field.metadata
            field_type = metadata["type"]
            if field_type == 's':
                field_size = 1
            elif field_type in ['I', 'i', 'f']:
                field_size = metadata.get("values", 1)
            else:
                field_size = 1
            size_list[metadata["pos"]] = field_size
        
        pos_list = [0]
        for i in range(1, len(size_list)):
            pos_list.append(pos_list[i-1] + size_list[i-1])
        
        return pos_list
    

    @classmethod
    def _pack_size(cls):
        """
        only used with to_bytes function
        returns the size of the data fields in terms of the
        struct unpack function return
        """
        size = 0
        for field in cls.__dataclass_fields__.values():
            metadata: fieldmeta = field.metadata
            field_type = metadata["type"]
            if field_type == 's':
                field_size = 1
            elif field_type in ['I', 'i', 'f']:
                field_size = metadata.get("values", 1)
            else:
                field_size = 1
            size += field_size
        return size
    

    def get_byte_size(self) -> int:
        pass
        


class PataponDynamicDataClass(PataponDataClass):
    byte_order: str = "<"
    @classmethod
    def from_bytes(cls, raw: bytes, *_, header: PataponDataClassHeader | PataponDataClass | None = None) -> 'PataponDynamicDataClass':
        field_class: type[PataponDataClass]
        new_value: PataponDataClass | Any
        new_inst: PataponDynamicDataClass = cls()

        # base case for empty header/body
        if len(raw) == 0:
            return new_inst

        for name, field in cls._ordered_dataclass_fields():
            data_type = field.metadata["type"]
            data_size = field.metadata.get("data_size", 0)

            if data_type == "header":
                field_class = field.type
                if data_size != 0:
                    # static header
                    raw_header = raw[:data_size]
                    new_value = field_class.from_bytes(raw_header)
                else:
                    # dynamic header
                    new_value = field_class.from_bytes(raw)
                    data_size = new_value.get_byte_size()
            elif data_type == "body":
                field_class = field.type
                # find the matching header class for body
                headers = cls.find_name_by_tag(field.metadata["tag"], type_search="header")
                new_header_name = headers[0] if len(headers) > 0 else None
                if new_header_name is not None:
                    new_header = getattr(new_inst, new_header_name)
                else:
                    header = None

                if data_size != 0:
                    # static body
                    raw_body = raw[:data_size]
                    new_value = field_class.from_bytes(raw_body, header=new_header)
                else:
                    # dynamic body
                    new_value = field_class.from_bytes(raw, header=new_header)
                    data_size = new_value.get_byte_size()
            else:
                # primary types
                field_tag = field.metadata.get("tag", "")
                field_tag_type = field.metadata.get("tag_type", "")

                if field_tag != "":
                    # check header for tag first
                    if isinstance(header, PataponDataClass):
                        field_value = header.__class__.find_value_by_tag(header, field_tag)
                    else:
                        field_value = None
                    # check current inst for tag next if not found
                    if field_value == None:
                        field_value = cls.find_value_by_tag(new_inst, field_tag)

                    # created the format string based on tag type
                    if field_value is not None:
                        if field_tag_type == "size":
                            field_format_string = f"{field_value}{data_type}"
                        elif field_tag_type == "hex_size":
                            field_value //= calcsize(data_type)
                            field_format_string = f"{field_value}{data_type}"
                        elif field_tag_type == "count":
                            field_format_string = f"{data_type}" * field_value
                        elif field_tag_type == "func":
                            func: Callable[[], int] | None = field.metadata.get("func", None)
                            if func != None:
                                func_args = field.metadata.get("func_args", {})
                                new_func_args = {}
                                for arg, arg_tag in func_args.items():
                                    # check header for tag first
                                    if isinstance(header, PataponDataClass):
                                        arg_value = header.__class__.find_value_by_tag(header, arg_tag)
                                    else:
                                        arg_value = None
                                    # check current inst for tag next if not found
                                    if arg_value == None:
                                        arg_value = cls.find_value_by_tag(new_inst, arg_tag)
                                    new_func_args[arg] = arg_value or 0
                                field_value = func(**new_func_args)
                                field_format_string = f"{field_value}{data_type}"
                            else:
                                field_format_string = ""
                        else:
                            field_format_string = ""
                    else:
                        field_format_string = ""
                else:
                    # no tags, so just grab info from current field
                    field_size = field.metadata.get("size", None)
                    field_values = field.metadata.get("values", None)
                    count = field_size or field_values or ""
                    field_format_string = f"{count}{data_type}"
                
                # extract the value from raw bytes
                data_size = calcsize(field_format_string)
                new_value = unpack(field_format_string, raw[:data_size])

                # convert into correct datatype
                if data_type == "s":
                    encoding = field.metadata.get("encoding", "")
                    if encoding != "":
                        new_value = str(new_value[0]).encode(encoding)
                    else:
                        new_value = new_value[0]
                elif data_type in ['I', 'i', 'f']:
                    filler_values = field.metadata.get("values", -1)

                    # only really used for filler at this point
                    if filler_values != -1:
                        new_value = list(new_value)
                    else:
                        new_value = new_value[0]
                elif data_type == 'x':
                    new_value = b'\x00' * field_value
                else:
                    new_value = new_value[0]

            # set the new value and remove processes value from the raw bytes
            setattr(new_inst, name, new_value)
            raw = raw[data_size:]
        
        return new_inst


    def to_bytes(self) -> bytes:
        pass
            
            
    @classmethod
    def format_string(cls) -> str:
        pass


    def get_byte_size(self) -> int:
        cls = self.__class__
        size = 0
        for name in cls.__dataclass_fields__.keys():
            value = getattr(self, name)
            
            if isinstance(value, (PataponStaticDataClass, PataponDynamicDataClass)):
                size += value.get_byte_size()
            elif isinstance(value, (str, bytes)):
                size += len(value)
            elif isinstance(value, (int, float)):
                size += 4
            elif isinstance(value, list):
                size += len(value) * cls.get_byte_size(value[0])
            else:
                raise NotImplementedError(f"uh oh, we are not supposed to be expecting other values in get_byte_size: {type(value)}")
        return size


    @classmethod
    def _ordered_dataclass_fields(cls) -> list[tuple[str,Field] | tuple]:
        ordered: list[tuple[str,Field] | tuple] = list(() for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: fieldmeta = field.metadata
            ordered[metadata["pos"]] = (name, field)
        
        return ordered