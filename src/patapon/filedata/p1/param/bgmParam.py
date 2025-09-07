from dataclasses import dataclass, field 
from patapon.filedata.patapon_data_class import (
    PataponStaticDataClass,
    FieldMetadata
)



@dataclass
class BGMParam(PataponStaticDataClass):
    bgm_info: str = field(default="", metadata={"meta": FieldMetadata("string", 0, size=0xF)})


    def getDefaultBgmVolume(self) -> float:
        return int(self.bgm_info.split(";\r\n")[0])
    

    def getSecondEntry(self) -> float:
        return float(self.bgm_info.split(";")[1])


    def getUserid(self) -> int:
        return int(self.bgm_info.split(";")[2])