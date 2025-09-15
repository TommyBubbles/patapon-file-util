from dataclasses import dataclass, field
from patapon.filedata.patapon_data_class import (
    PataponDynamicDataClass,
    FieldMetadata
)


@dataclass
class UnknownDataClass(PataponDynamicDataClass):
    data: bytes = field(default=b'', metadata={"meta": FieldMetadata("bytes", 0, size=-1)})