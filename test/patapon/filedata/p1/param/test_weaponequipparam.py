from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import WeaponParam, EquipParam
from patapon.filedata.p1.param.weaponequipparam import (
    WeaponParamHeader
)
from patapon.filedata.p1.param import DamageParam
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



class Test_WeaponParam:
    @fixture
    def weapon_param_header(self) -> WeaponParamHeader:
        return WeaponParamHeader(
            b'YGF_GFP\x00',
            0x40,
            0.800000011920929,
            0x1,
            [0,0,0],
            [
                GenericParamHeaderPartitionInfo(0x100, 0x1A0)
            ],
            b'\x00\x00\x00\x00' * 6
        )


    @fixture
    def equip_param_last_element(self) -> EquipParam:
        return EquipParam(
            b'hlm030_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            255,
            [0, 0, 0],
            0,
            1,
            -1,
            0,
            -1,
            [0, 0, 0, 0, 0, 0, 0],
            DamageParam(
                -1.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0,
                0.0,
                -1,
                0.0,
                0.0,
                0.0,
                -1,
                -1,
                0,
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                b'8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [-1, -1, -1, -1, -1, -1, -1, -1]
            ),
            b'hlm000_0_030.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        )



    def test_verify_datafield_pos(self):
        assert WeaponParam.verify_datafield_pos()


    def test_get_byte_size(self,
            weapon_param_header: WeaponParamHeader,
            equip_param_last_element: EquipParam
            ):
        assert weapon_param_header.get_byte_size() == 0x40
        assert equip_param_last_element.get_byte_size() == 0x1A0


    def test_from_bytes(self,
            weapon_param_header: WeaponParamHeader,
            equip_param_last_element: EquipParam
            ):
        file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\weaponparam.dat"
        with open(file_name, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: WeaponParam = WeaponParam.from_bytes(data_stream)
            assert WeaponParam.verify_filler(actual)

        assert actual.header.get_byte_size() == 0x40
        assert actual.header == weapon_param_header

        assert len(actual.equip_params.param_list) == 0x100
        assert actual.equip_params.param_list[-1].get_byte_size() == 0x1A0
        assert actual.equip_params.param_list[-1] == equip_param_last_element



class Test_EquipParam:
    @fixture
    def file_one(self) -> str:
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\actor\\equip\\@hlm001_01\\equipparam.dat"
    

    @fixture
    def file_two(self) -> str:
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\actor\\equip\\@sld001_01\\equipparam.dat"


    @fixture
    def equip_param_file_one(self) -> EquipParam:
        return EquipParam(
            b'hlm001_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            140,
            [0, 0, 0],
            0,
            1,
            -1,
            0,
            -1,
            [0, 0, 0, 0, 0, 0, 0],
            DamageParam(
                0.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0,
                0.0,
                -1,
                0.0,
                0.0,
                0.0,
                -1,
                -1,
                0,
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [-1, -1, -1, -1, -1, -1, -1, -1]
            ),
            b'hlm000_0_001.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        )
    

    @fixture
    def equip_param_file_two(self) -> EquipParam:
        return EquipParam(
            b'sld001_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            215,
            [0, 0, 0],
            0,
            2,
            3,
            0,
            -1,
            [0, 0, 0, 0, 0, 0, 0],
            DamageParam(
                0.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0,
                0.0,
                -1,
                0.0,
                0.0,
                0.0,
                -1,
                -1,
                0,
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [-1, -1, -1, -1, -1, -1, -1, -1]
            ),
            b'sld001_001.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        )



    def test_verify_datafield_pos(self):
        assert EquipParam.verify_datafield_pos()


    def test_from_bytes_file_one(self,
            file_one: str,
            equip_param_file_one: EquipParam
            ):
        with open(file_one, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: EquipParam = EquipParam.from_bytes(data_stream)
            assert EquipParam.verify_filler(actual)

        assert actual.get_byte_size() == 0x1A0
        assert actual == equip_param_file_one

    
    def test_from_bytes_file_two(self,
            file_two: str,
            equip_param_file_two: EquipParam
            ):
        with open(file_two, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: EquipParam = EquipParam.from_bytes(data_stream)
            assert EquipParam.verify_filler(actual)

        assert actual.get_byte_size() == 0x1A0
        assert actual == equip_param_file_two