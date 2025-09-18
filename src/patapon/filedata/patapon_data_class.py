from struct import pack, unpack, calcsize, error
from dataclasses import dataclass, Field, field
from typing import Any, Callable, Union, get_origin, get_args
from enum import Enum, auto


class FieldType(Enum):
    bytes = auto()
    string = auto()
    padding = auto()
    signed_int = auto()
    unsigned_int = auto()
    signed_int16 = auto()
    unsigned_int16 = auto()
    signed_int8 = auto()
    unsigned_int8 = auto()
    float = auto()
    dataclass = auto()
    bnd_files = auto()


class FieldTagType(Enum):
    source = auto()
    size = auto()
    byte_size = auto()
    count = auto()
    byte_count = auto()
    header = auto()
    body = auto()
    list = auto()
    linked_list = auto()


class FieldTag:
    def __init__(self,
                 name: str,
                 tag_type: Any,
                 pos: int | None = None,
                 sub_tag: 'FieldTag | None' = None, 
                 *_,
                 func: Callable | None = None,
                 func_params: dict[str,str] | None = None):
        self.name = name
        self.tag_type = FieldTagType[tag_type]
        self.pos = pos
        self.sub_tag = sub_tag
        self.func = func
        self.func_params = func_params


class FieldMetadata:
    def __init__(self,
                 field_type: Any,
                 pos: int,
                 *_,
                 size: int = 1,
                 count: int = 1,
                 data_size: int = 0,
                 byte_order: str | None = None,
                 encoding: str = "utf-8"
                 ):
        self.field_type = FieldType[field_type]
        self.pos = pos
        self.size = size
        self.count = count
        self.data_size = data_size
        self.byte_order = byte_order
        self.encoding = encoding

        if encoding == 'shift-jis':
            self.char_width = 2
            self.null_term = b'\x00\x00'
        else:
            self.char_width = 1
            self.null_term = b'\x00'


    def get_field_string(self) -> str:
        format_string_dict: dict[FieldType,str] = {
            FieldType.bytes: "s",
            FieldType.string: "s",
            FieldType.padding: "x",
            FieldType.signed_int: "i",
            FieldType.unsigned_int: "I",
            FieldType.signed_int16: "h",
            FieldType.unsigned_int16: "H",
            FieldType.signed_int8: "b",
            FieldType.unsigned_int8: "B",
            FieldType.float: "f"
        }
        return format_string_dict.get(self.field_type, "")


    def get_from_bytes_func(self) -> Callable:
        func_dict = {
            FieldType.string: lambda x: bytes(x).decode(self.encoding),
            FieldType.bytes: lambda x: bytes(x),
            FieldType.padding: lambda _: self.size * b'\x00',
            FieldType.signed_int: lambda x: int(x),
            FieldType.unsigned_int: lambda x: int(x),
            FieldType.signed_int16: lambda x: int(x),
            FieldType.unsigned_int16: lambda x: int(x),
            FieldType.signed_int8: lambda x: int(x),
            FieldType.unsigned_int8: lambda x: int(x),
            FieldType.float: lambda x: float(x)
        }
        return func_dict.get(self.field_type, lambda x: x)
    

    def get_to_bytes_func(self) -> Callable:
        func_dict = {
            FieldType.string: lambda x: str(x).encode(self.encoding),
            FieldType.bytes: lambda x: bytes(x),
            FieldType.padding: lambda x: bytes(x),
            FieldType.signed_int: lambda x: int(x),
            FieldType.unsigned_int: lambda x: int(x),
            FieldType.signed_int16: lambda x: int(x),
            FieldType.unsigned_int16: lambda x: int(x),
            FieldType.signed_int8: lambda x: int(x),
            FieldType.unsigned_int8: lambda x: int(x),
            FieldType.float: lambda x: float(x)
        }

        return func_dict.get(self.field_type, lambda x: x)


    def get_byte_size_single(self) -> int:
        return calcsize(self.get_field_string())


    def get_byte_size(self) -> int:
        count: int = self.count
        size: int = self.size
        field_string_size: int = self.get_byte_size_single()
        return size * field_string_size * count


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


class PataponDataClassElement:
    _offset: int
    

    def __init__(self):
        pass


    @property
    def offset(self) -> int:
        if hasattr(self, "_offset"):
            return self._offset
        return -1


    @offset.setter
    def offset(self, val: int) -> None:
        self._offset = val


@dataclass
class PataponDataClass:
    @classmethod
    def from_bytes(cls, raw: bytes, *, header: 'PataponDataClass | None' = ...) -> 'PataponDataClass': ...
    @classmethod
    def format_string(cls) -> str: ...
    def to_bytes(self) -> bytes: ...
    def process(self, raw: bytes) -> tuple[int,Any]: ...


    def __init__(self):
        pass


    def get_byte_size(self, start: int = 0, end: int = -1) -> int:
        cls = self.__class__
        size = 0
        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata['meta']
            if metadata.pos < start or (end != -1 and metadata.pos >= end):
                continue

            value = getattr(self, name)
            if isinstance(value, PataponDataClass):
                size += value.get_byte_size()
            elif isinstance(value, (int, float)):
                size += metadata.get_byte_size()
            elif isinstance(value, (bytes, str)):
                if len(value) != 0:
                    size += max(metadata.get_byte_size(), metadata.get_byte_size_single() * len(value))
            elif isinstance(value, list):
                if len(value) > 0:
                    if isinstance(value[0], (int, float)):
                        size += metadata.get_byte_size_single() * len(value)
                    elif isinstance(value[0], (bytes, str)):
                        temp_size = 0
                        for i in value:
                            temp_size += metadata.get_byte_size_single() * len(i)
                        size += max(metadata.get_byte_size(), temp_size)
                    elif isinstance(value[0], PataponDataClass):
                        for i in value:
                            size += i.get_byte_size()
                    else:
                        raise NotImplementedError(f"uh oh, we are not supposed to be expecting other values in {self.__class__.__name__}.get_byte_size: {type(value)}")
            else:
                raise NotImplementedError(f"uh oh, we are not supposed to be expecting other values in {self.__class__}.get_byte_size: {type(value)}")
        return size


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
            tags: list[FieldTag] = field.metadata.get("tags", [])
            for tag in tags:
                if tag.name == tag_name and \
                        (exclude is None or name != exclude):
                    results.append(tag)
                    break
            
        return results[0] if len(results) > 0 else None


    @classmethod
    def add_tag_to_field(cls, name: str, tag: FieldTag):
        field_info = cls.__dataclass_fields__.get(name, None)

        if field_info is not None:
            if field_info.metadata.get("tags", None) == None:
                field_info.metadata["tags"] = []
            field_info.metadata["tags"].append(tag)


    @classmethod
    def eval_tag(cls, new_inst: 'PataponDataClass', header: 'PataponDataClass | None', tag: FieldTag) -> int:
        def get_tag_value(check_cls: type[PataponDataClass], obj: PataponDataClass, tag_name: str):
            obj_field_value = check_cls.get_field_value_by_tag_name(obj, tag_name, tag_type_search=FieldTagType.source)
            if obj_field_value is not None:
                if type(obj_field_value) == int:
                    return obj_field_value
                elif type(obj_field_value) == list:
                    source_tag = check_cls.get_tag_by_name(tag_name)
                    if tag.pos is not None and tag.sub_tag is not None:
                        list_pos = tag.pos
                        sub_tag = tag.sub_tag
                    elif source_tag is not None and source_tag.pos is not None and source_tag.sub_tag is not None:
                        list_pos = source_tag.pos
                        sub_tag = source_tag.sub_tag
                    else:
                        return obj_field_value
                        # raise LookupError(f"Unable to find tag information for {tag.name}: pos and sub_tag")
                    
                    index_value = obj_field_value[list_pos]
                    if isinstance(index_value, PataponDataClass):
                        return index_value.__class__.eval_tag(index_value, None, sub_tag)
                    else:
                        return index_value
            return None

        if tag.func is not None:
            func: Callable[..., int]= tag.func
            params = tag.func_params or {}
            new_params = {}
            for param_name, tag_name in params.items():
                new_param_value = None
                if tag_name == 'self':
                    new_param_value = new_inst

                # check new instance for tag first
                if new_param_value is None:
                    new_param_value = get_tag_value(cls, new_inst, tag_name)

                # check header for tag second
                if new_param_value is None and isinstance(header, PataponDataClass):
                    new_param_value = get_tag_value(header.__class__, header, tag_name)

                new_params[param_name] = new_param_value
            return func(**new_params)
        else: 
            # check new instance for tag first
            field_value = get_tag_value(cls, new_inst, tag.name)

            # check header for tag second
            if isinstance(header, PataponDataClass) and field_value is None:
                field_value = get_tag_value(header.__class__, header, tag.name)

            if field_value is not None:
                return field_value
            
        raise LookupError(f"Unable to find tag {tag.name}")


    @classmethod
    def _ordered_dataclass_fields(cls) -> list[tuple[str,Field] | tuple]:
        ordered: list[tuple[str,Field] | tuple] = list(() for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata["meta"]
            ordered[metadata.pos] = (name, field)
        
        return ordered


    @classmethod
    def verify_filler(cls, obj: 'PataponDataClass', *_, path: str = '') -> bool:
        zeroflag = True
        for field in cls.__dataclass_fields__.keys():
            value = getattr(obj, field)
            if field.startswith('filler'):
                if isinstance(value, list):
                    for val in value:
                        if val != 0:
                            print(f"non-zero value found in {path}{field}: {val}")
                            zeroflag = False
                elif value != 0:
                    print(f"non-zero value found in {path}{field}: {value}")
                    zeroflag = False
            elif isinstance(value, PataponDataClass):
                value_cls = value.__class__
                zeroflag = value_cls.verify_filler(value, path=path + field + ".")
            elif isinstance(value, list):
                for val in value:
                    if isinstance(val, PataponDataClass):
                        val_cls = val.__class__
                        zeroflag = val_cls.verify_filler(val, path=path + field + ".")
        return zeroflag
    

    @classmethod
    def verify_datafield_pos(cls, path: str = ""):
        field_list: list[list] = list([] for _ in cls.__dataclass_fields__.values())

        for name, field in cls.__dataclass_fields__.items():
            metadata: FieldMetadata = field.metadata["meta"]
            field_list[metadata.pos].append(f"{path}{name}")

            if issubclass(field.type, PataponDataClass):
                field.type.verify_datafield_pos(f"{path}{name}.")
            elif get_origin(field.type) == list and issubclass(get_args(field.type)[0], PataponDataClass):
                get_args(field.type)[0].verify_datafield_pos(f"{path}{name}.")

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
    

    def ordered_field_names(self):
        return list(item[0] for item in self.__class__._ordered_dataclass_fields())


    def tsv_header(self) -> str:
        tsv_header_list = []
        for name in self.ordered_field_names():
            if name.startswith("filler"):
                continue

            val: Any = getattr(self, name)
            if isinstance(val, PataponDataClass):
                tsv_header_list.append(val.tsv_header())
            else:
                tsv_header_list.append(name)
        return "\t".join(tsv_header_list)


    def tsv(self) -> str:
        tsv_list = []
        for name in self.ordered_field_names():
            if name.startswith("filler"):
                continue

            val: Any = getattr(self, name)
            if isinstance(val, PataponDataClass):
                tsv_list.append(val.tsv())
            elif isinstance(val, str):
                tsv_list.append(val.strip("\0"))
            else:
                tsv_list.append(str(val))
        return "\t".join(tsv_list)
    


class PataponStaticDataClass(PataponDataClass):
    byte_order: str = "<"
    @classmethod
    def from_bytes(cls, raw: bytes, *_, **__) -> 'PataponStaticDataClass':
        new_inst = cls()
        format_string = cls.format_string()

        # base case for empty header/body
        try:
            size = calcsize(format_string)
        except error:
            raise error(f"class: {cls.__name__}, format_string: {format_string}")
        try:
            if size == 0:
                return new_inst
            raw_values = unpack(format_string, raw[:size])
        except error as err:
            raise error(f"error msg: {err.args[0]}, class: {cls.__name__}, format_string: {format_string}, raw: {raw[:size]}, raw size: {len(raw)}")


        index = 0
        for name, field in cls._ordered_dataclass_fields():
            metadata: FieldMetadata = field.metadata["meta"]
            count: int = metadata.count
            func: Callable = metadata.get_from_bytes_func()
            try:
                if count > 1:
                    new_value = list(func(value) for value in raw_values[index:index + count])
                else:
                    new_value = func(raw_values[index])
            except UnicodeDecodeError as err:
                raise TypeError(f"Error with field {cls.__name__}.{name}: {err.reason} {err.object}")
                
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



class PataponDynamicDataClass(PataponDataClass):
    byte_order: str = "<"
    @classmethod
    def from_bytes(cls, raw: bytes, *_, header: Union[PataponDataClass,None] = None, file_offset: int = 0) -> 'PataponDynamicDataClass':
        new_value: PataponDataClass | Any
        new_inst: PataponDynamicDataClass = cls()

        # base case for empty header/body
        if len(raw) == 0:
            return new_inst

        for name, field in cls._ordered_dataclass_fields():
            metadata: FieldMetadata = field.metadata["meta"]
            field_type: FieldType = metadata.field_type
            data_size: int = metadata.data_size

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

            if field_type == FieldType.bnd_files:
                data_size, new_value = new_inst.process(raw)
                pass
            elif field_type == FieldType.dataclass:
                field_class: type[PataponDataClass]
                if get_origin(field.type) == list:
                    field_class = get_args(field.type)[0]
                else:
                    field_class = field.type
                
                if get_origin(field.type) == list:
                    byte_size_tag = new_inst.get_tag_by_type(FieldTagType.byte_size, field_name=name)
                    linked_list_tag = new_inst.get_tag_by_type(FieldTagType.linked_list, field_name=name)

                    if byte_size_tag is not None:
                        byte_size = cls.eval_tag(new_inst, header, byte_size_tag)

                        new_value = []
                        offset = 0
                        while offset < byte_size:
                            new_element: Union[PataponDataClass,PataponDataClassElement] = field_class.from_bytes(raw[offset:], header=header)
                            new_element.offset = offset
                            new_value.append(new_element)
                            offset += new_element.get_byte_size()
                        data_size = offset
                    elif linked_list_tag is not None:
                        # linked list
                        new_value = []
                        offset = 0
                        index = 0
                        new_element = cls()
                        while True:
                            if not cls.eval_tag(new_inst, new_element, linked_list_tag):
                                break
                            new_element: PataponDataClass = field_class.from_bytes(raw[offset:])
                            new_element.offset = offset
                            new_value.append(new_element)
                            offset += new_element.get_byte_size()
                            index += 1
                            
                        data_size = offset
                    else:
                        new_value = []
                        offset = 0
                        for _ in range(count):
                            new_element = field_class.from_bytes(raw[offset:], header=header)
                            new_element.offset = offset
                            new_value.append(new_element)
                            offset += new_element.get_byte_size()
                        data_size = offset
                else:
                    # find the matching header class for body, if applicable
                    body_tag: FieldTag | None = cls.get_tag_by_type(FieldTagType.body, field_name=name)
                    new_header = None
                    if body_tag is not None:
                        headers = cls.get_field_name_by_tag_name(body_tag.name, field_type_search=FieldType.dataclass, tag_type_search=FieldTagType.header)
                        if len(headers) > 0:
                            new_header = getattr(new_inst, headers[0])
                    
                    new_value = field_class.from_bytes(raw, header=new_header)
                    data_size = new_value.get_byte_size()
            else:
                # primary types
                size: int
                count: int
                field_format_string = ""

                # byte size and byte count are only really used in special cases
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

                # in the case of a string, we have to check if a size was given
                # if not, we must try to find the correct size to extract from the
                # bytes by using a null terminator
                if metadata.field_type == FieldType.string and size == 1:
                    size_array = []
                    
                    null_term = metadata.null_term
                    end = 0
                    prev_end = 0
                    for _ in range(count):
                        while end < len(raw) and null_term != raw[end:end+metadata.char_width]:
                            end=end+metadata.char_width
                        size_array.append(min(end+metadata.char_width-prev_end, len(raw)))
                        end = end+metadata.char_width
                        prev_end = end
                    field_format_string = "".join(f"{s}{metadata.get_field_string()}" for s in size_array)
                    

                # in the case of bytes, we have to check if a size of -1 was given
                # if so, read in the rest of the data stream as bytes
                if metadata.field_type == FieldType.bytes and size == -1:
                    size = len(raw)

                # construct the format string to be used with unpack function
                if field_format_string == "":
                    field_format_string = f"{size}{metadata.get_field_string()}" * count
                field_byte_order = metadata.byte_order or cls.byte_order

                # extract the value from raw bytes
                field_format_string = field_byte_order + field_format_string
                try:
                    data_size = calcsize(field_format_string)
                    if data_size == 0:
                        continue
                    new_values = unpack(field_format_string, raw[:data_size])
                except error as err:
                    raise error(f"{name}: {field_format_string}")

                # process the raw values into correct data types
                try:
                    func: Callable = metadata.get_from_bytes_func()
                    if count > 1 or get_origin(field.default_factory) == list:
                        new_value = list(func(val) for val in new_values)
                    elif len(new_values) == 0:
                        new_value = b'\x00' * size
                    else:
                        new_value = func(new_values[0])
                except UnicodeDecodeError as err:
                    raise TypeError(f"Error with field: {name}: {err.reason}")
                    # raise TypeError(f"Error with field: {name}: {err.reason} {err.object}")

            # set the new value and remove processed value from the raw bytes
            setattr(new_inst, name, new_value)
            raw = raw[data_size:]
        
        return new_inst


    def to_bytes(self) -> bytes:
        return b''
            
            
    @classmethod
    def format_string(cls) -> str:
        return ""


def new_data_field(metadata: FieldMetadata, *_, field_type: type | None = None, tags: list[FieldTag] = []):
    field_metadata = {
        "meta": metadata,
        "tags": tags
    }
    if field_type != None and issubclass(field_type, PataponDataClass):
        return field(default_factory=field_type, metadata=field_metadata)
    return field(default=None, metadata=field_metadata)