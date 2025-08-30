from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import PataponStaticDataClass, PataponDynamicDataClass, PataponDataClassBody, PataponDataClassHeader, PataponDataClassElement, FieldMetadata, FieldTag


@dataclass
class ItemMessageHeader(PataponStaticDataClass, PataponDataClassHeader):
    message_count: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("message_count", "source")]})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})



@dataclass
class ItemMessageOffsetList(PataponDynamicDataClass, PataponDataClassBody):
    message_offsets: list[int] = field(default_factory=list[int], metadata={"meta": FieldMetadata("unsigned_int", 0), "tags": [FieldTag("message_count", "count")]})
    filler_1: int = field(default=0, metadata={"meta": FieldMetadata("unsigned_int", 1)})



@dataclass
class ItemMessageElement(PataponDynamicDataClass, PataponDataClassElement):
    message: str = field(default="", metadata={"meta": FieldMetadata("string", 0, encoding="shift-jis", char_width=2, null_term=b'\x00\x00')})


@dataclass
class ItemMessageList(PataponDynamicDataClass, PataponDataClassBody):
    message_list: list[ItemMessageElement] = field(default_factory=list[ItemMessageElement], metadata={"meta": FieldMetadata("element_list", 0), "tags": [FieldTag("message_count", "count")]})



@dataclass
class ItemMessage(PataponDynamicDataClass):
    header: ItemMessageHeader = field(default_factory=ItemMessageHeader, metadata={"meta": FieldMetadata("header", 0), "tags": [FieldTag("file", "header")]})
    item_message_offsets: ItemMessageOffsetList = field(default_factory=ItemMessageOffsetList, metadata={"meta": FieldMetadata("body", 1), "tags": [FieldTag("file", "body")]})
    item_messages: ItemMessageList = field(default_factory=ItemMessageList, metadata={"meta": FieldMetadata("body", 2), "tags": [FieldTag("file", "body")]})


    def find_message_by_index(self, index: int) -> str:
        if index > len(self.item_message_offsets.message_offsets):
            return ""
        
        offset = self.item_message_offsets.message_offsets[index]

        for message in self.item_messages.message_list:
            list_offset = offset - self.item_message_offsets.get_byte_size() - self.header.get_byte_size()
            if message.offset == list_offset:
                return message.message
        
        return ""
        
        