from struct import pack, unpack, calcsize
from dataclasses import dataclass, Field
from typing import Any, Callable, get_origin, List
from enum import Enum


class FieldType(Enum):
    bytes = 0
    string = 1
    padding = 2
    signed_int = 3
    unsigned_int = 4
    float = 5
    header = 6
    body = 7


class FieldTagType(Enum):
    source = 0
    size = 1
    byte_size = 2
    count = 3
    byte_count = 4
    header = 5
    body = 6


class FieldTag():
    def __init__(self,
                 name: str,
                 tag_type: Any,
                 *_,
                 func: Callable | None = None,
                 func_params: dict[str,str] | None = None):
        self.name = name
        self.tag_type = FieldTagType[tag_type]
        self.func = func
        self.func_params = func_params


class FieldMetadata():
    def __init__(self,
                 field_type: Any,
                 pos: int,
                 *_,
                 size: int = 1,
                 count: int = 1,
                 data_size: int = 0,
                 encoding: str = "utf-8",
                 byte_order: str | None = None):
        self.field_type = FieldType[field_type]
        self.pos = pos
        self.size = size
        self.count = count
        self.data_size = data_size
        self.encoding = encoding
        self.byte_order = byte_order


    def get_field_string(self) -> str:
        format_string_dict: dict[FieldType,str] = {
            FieldType.bytes: "s",
            FieldType.string: "s",
            FieldType.padding: "x",
            FieldType.signed_int: "i",
            FieldType.unsigned_int: "I",
            FieldType.float: "f"
        }
        return format_string_dict.get(self.field_type, "")
    

    def get_from_bytes_func(self) -> Callable:
        func_dict = {
            FieldType.string: lambda x: bytes(x).decode(self.encoding).strip('\x00'),
            FieldType.bytes: lambda x: bytes(x),
            FieldType.padding: lambda _: self.size * b'\x00',
            FieldType.signed_int: lambda x: int(x),
            FieldType.unsigned_int: lambda x: int(x),
            FieldType.float: lambda x: float(x)
        }

        return func_dict.get(self.field_type, lambda x: x)
    

    def get_to_bytes_func(self) -> Callable:
        func_dict = {
            FieldType.string: lambda x: str(x).encode(self.encoding) + b'\x00' * (self.size - len(x)),
            FieldType.bytes: lambda x: bytes(x),
            FieldType.padding: lambda x: bytes(x),
            FieldType.signed_int: lambda x: int(x),
            FieldType.unsigned_int: lambda x: int(x),
            FieldType.float: lambda x: float(x)
        }

        return func_dict.get(self.field_type, lambda x: x)
    

    def get_byte_size(self) -> int:
        count: int = self.count
        size: int = self.size
        field_string_size: int = calcsize(self.get_field_string())
        return size * field_string_size * count


    def get_pos_size(self) -> int:
        count: int = self.count
        return count


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
    def get_tag_list(self) -> dict[str,str]: ...


    def __init__(self):
        pass


    @classmethod
    def get_field_name_by_tag_name(cls, tag_name: str, *_,
                                   field_type_search: FieldType | None = None,
                                   tag_type_search: FieldTagType | None = None, 
                                   exclude: str | None = None) -> list[str]:
        results = []

        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata["meta"]
            tags: list[FieldTag] = field.metadata.get("tags", [])
            for tag in tags:
                if tag.name == tag_name and \
                        (field_type_search is None or metadata.field_type == field_type_search) and \
                        (tag_type_search is None or tag.tag_type == tag_type_search) and \
                        (exclude == None or name != exclude):
                    results.append(name)
                    break
            
        return results
    

    @classmethod
    def get_field_value_by_tag_name(cls, obj: 'PataponDataClass', tag: str, *_, **kwargs) -> Any:
        fields = cls.get_field_name_by_tag_name(tag, **kwargs)
        if len(fields) == 1:
            field_value = getattr(obj, fields[0])
        elif len(fields) > 1:
            raise LookupError(f'Too many fields in {obj} with the same tag: {fields}')
        else:
            field_value = None
        return field_value


    @classmethod
    def get_tag_by_type(cls, tag_type: FieldTagType, *_, field_name: str | None = None) -> FieldTag | None:
        results: list[FieldTag] = []

        for name, field in cls.__dataclass_fields__.items():
            tags: list[FieldTag] = field.metadata.get("tags", [])
            for tag in tags:
                if tag.tag_type == tag_type and \
                    (field_name is None or name == field_name):
                    results.append(tag)
                    break
            
        return results[0] if len(results) > 0 else None
        

    @classmethod
    def get_tag_by_name(cls, tag_name: str, *_, exclude: str | None = None) -> FieldTag | None:
        results: list[FieldTag] = []

        for name, field in cls.__dataclass_fields__.items():
            tags: list[FieldTag] = field.metadata("tags", [])
            for tag in tags:
                if tag.name == tag_name and \
                        (exclude is None or name != exclude):
                    results.append(tag)
                    break
            
        return results[0] if len(results) > 0 else None


    @classmethod
    def _ordered_dataclass_fields(cls) -> list[tuple[str,Field] | tuple]:
        ordered: list[tuple[str,Field] | tuple] = list(() for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata["meta"]
            ordered[metadata.pos] = (name, field)
        
        return ordered


    @classmethod
    def verify_filler(cls, obj: 'PataponDataClass') -> bool:
        zeroflag = True
        for field in cls.__dataclass_fields__.keys():
            if field.startswith('filler'):
                value = getattr(obj, field)

                if type(value) == list:
                    for val in getattr(obj, field):
                        if val != 0:
                            print(f"non-zero value found in {field}: {val}")
                            zeroflag = False
                elif type(value) == PataponDataClass:
                    zeroflag = cls.verify_filler(value)
                else:
                    if value != 0:
                        print(f"non-zero value found in {field}: {value}")
                        zeroflag = False
        return zeroflag
    

    @classmethod
    def verify_datafield_pos(cls):
        field_list: list[list] = list([] for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata["meta"]
            field_list[metadata.pos].append(name)

        valid = True
        for i in range(len(field_list)):
            item: list = field_list[i]
            if len(item) == 0:
                print(f"no fields found at position {i}")
                valid = False
            elif len(item) >= 2:
                print(f"too many fields found at position {i}: {item}")
                valid = False

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
        index = 0
        for name, field in cls._ordered_dataclass_fields():
            metadata: FieldMetadata = field.metadata["meta"]
            count: int = metadata.count
            func: Callable = metadata.get_from_bytes_func()
            
            if count > 1:
                new_value = list(func(value) for value in raw_values[index:index + count])
            else:
                new_value = func(raw_values[index])
            setattr(new_inst, name, new_value)
            index += count
        return new_inst
    

    def to_bytes(self) -> bytes:
        cls = self.__class__
        format_string = cls.format_string()
        
        # base case for empty header/body
        if calcsize(format_string):
            return b''

        values = []
        for name, field in cls._ordered_dataclass_fields():
            metadata: FieldMetadata = field.metadata["meta"]
            func: Callable = metadata.get_to_bytes_func()
            value = getattr(self, name)

            if type(value) == list:
                values.extend(list(func(val) for val in value))
            else:
                values.append(func(value))

        return pack(format_string, *values)
            
            
    @classmethod
    def format_string(cls) -> str:
        format_list = list("" for _ in cls.__dataclass_fields__.values())
        
        for field in cls.__dataclass_fields__.values():
            metadata: FieldMetadata = field.metadata["meta"]
            pos: int = metadata.pos
            count: int = metadata.count
            size: int = metadata.size
            field_string: str = metadata.get_field_string()
            
            format_list[pos] = f"{size}{field_string}" * count
        
        return cls.byte_order + "".join(format_list)
    

    def get_byte_size(self) -> int:
        cls = self.__class__
        
        size = 0
        for field in cls.__dataclass_fields__.values():
            metadata: FieldMetadata = field.metadata["meta"]
            size += metadata.get_byte_size()
        return size


class PataponDynamicDataClass(PataponDataClass):
    tag_list: dict[FieldTag,str] = {}
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
            metadata: FieldMetadata = field.metadata["meta"]
            field_type: FieldType = metadata.field_type
            data_size: int = metadata.data_size

            if field_type == FieldType.header:
                field_class = field.type
                if data_size != 0:
                    # static header
                    raw_header = raw[:data_size]
                    new_value = field_class.from_bytes(raw_header)
                else:
                    # dynamic header
                    new_value = field_class.from_bytes(raw)
                    data_size = new_value.get_byte_size()
            elif field_type == FieldType.body:
                field_class = field.type
                body_tag: FieldTag | None = cls.get_tag_by_type(FieldTagType.body, field_name=name)
                
                # find the matching header class for body
                if body_tag is not None:
                    headers = cls.get_field_name_by_tag_name(body_tag.name, field_type_search=FieldType.header, tag_type_search=FieldTagType.header)
                    new_header_name = headers[0] if len(headers) > 0 else None
                else:
                    new_header_name = None

                if new_header_name is not None:
                    new_header = getattr(new_inst, new_header_name)
                else:
                    new_header = None

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
                size: int
                count: int

                # get the size of the data field
                size_tag = new_inst.get_tag_by_type(FieldTagType.size, field_name=name)
                if size_tag is not None:
                    size = cls.eval_tag(new_inst, header, size_tag)
                else:
                    size = metadata.size

                # get the count of the data field
                count_tag = new_inst.get_tag_by_type(FieldTagType.count, field_name=name)
                if count_tag is not None:
                    count = cls.eval_tag(new_inst, header, count_tag)
                else:
                    count = metadata.count

                # byte size and hex count are only really used in special cases
                # where the size or count given by another field is the byte size
                # of it rather then the element size or count.
                # these should not be specified if their non-byte counterparts are given
                byte_size_tag = new_inst.get_tag_by_type(FieldTagType.byte_size, field_name=name)
                if byte_size_tag is not None:
                    size = cls.eval_tag(new_inst, header, byte_size_tag) // count
                
                byte_count_tag = new_inst.get_tag_by_type(FieldTagType.byte_count, field_name=name)
                if byte_count_tag is not None:
                    if get_origin(field.type) is list and size == 1:
                        element_size = calcsize(metadata.get_field_string())
                    else:
                        element_size = size
                    count = cls.eval_tag(new_inst, header, byte_count_tag) // element_size

                # construct the format string to be used with unpack function
                field_format_string = f"{size}{metadata.get_field_string()}" * count
                field_byte_order = metadata.byte_order or cls.byte_order

                # extract the value from raw bytes
                field_format_string = field_byte_order + field_format_string
                data_size = calcsize(field_format_string)
                new_values = unpack(field_format_string, raw[:data_size])

                # process the raw values into correct data types
                func: Callable = metadata.get_from_bytes_func()
                if count > 1:
                    new_value = list(func(val) for val in new_values)
                elif len(new_values) == 0:
                    new_value = b'\x00' * size
                else:
                    new_value = func(new_values[0])

            # set the new value and remove processes value from the raw bytes
            setattr(new_inst, name, new_value)
            raw = raw[data_size:]
        
        return new_inst

    @classmethod
    def eval_tag(cls, new_inst: PataponDataClass, header: PataponDataClassHeader | PataponDataClass | None, tag: FieldTag) -> int:
        if tag.func != None:
            func: Callable[..., int]= tag.func
            params = tag.func_params or {}
            new_params = {}
            for param_name, tag_name in params.items():
                new_param_value = None
                # check new instance for tag first
                new_inst_field_value = cls.get_field_value_by_tag_name(new_inst, tag_name, tag_type_search=FieldTagType.source)
                if new_inst_field_value is not None and type(new_inst_field_value) == int:
                    new_param_value = new_inst_field_value

                # check header for tag second
                if new_param_value is None and isinstance(header, PataponDataClass):
                    header_field_value = header.get_field_value_by_tag_name(header, tag_name, tag_type_search=FieldTagType.source)
                    if header_field_value is not None and type(header_field_value) == int:
                        new_param_value = header_field_value
                
                new_params[param_name] = new_param_value
            return func(**new_params)
        else: 
            # check new instance for tag first
            new_inst_field_value = cls.get_field_value_by_tag_name(new_inst, tag.name, tag_type_search=FieldTagType.source)
            if new_inst_field_value is not None and type(new_inst_field_value) == int:
                return new_inst_field_value

            # check header for tag second
            if isinstance(header, PataponDataClass):
                header_field_value = header.get_field_value_by_tag_name(header, tag.name, tag_type_search=FieldTagType.source)
                if header_field_value != None and type(header_field_value) == int:
                    return header_field_value
        raise LookupError(f"Unable to find tag {tag.name}")


    def to_bytes(self) -> bytes:
        return b''
            
            
    @classmethod
    def format_string(cls) -> str:
        return ""


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
                size += len(value) * len(bytes(value[0]))
            else:
                raise NotImplementedError(f"uh oh, we are not supposed to be expecting other values in get_byte_size: {type(value)}")
        return size