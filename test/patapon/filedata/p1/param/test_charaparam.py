from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CharaParam, BasesDataCharaParam
from patapon.filedata.p1.param.charaparam import (
    BasesDataCharaParamHeader
)
from patapon.filedata.p1.param import DamageParam
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


class Test_BasesDataCharaParam:
    @fixture
    def chara_param_header(self) -> BasesDataCharaParamHeader:
        return BasesDataCharaParamHeader(
            b'YGF_GFP\x00'.decode(),
            0x40,
            0.800000011920929,
            0x1,
            [0,0,0],
            [
                GenericParamHeaderPartitionInfo(0x29, 0x400)
            ],
            b'\x00\x00\x00\x00' * 6
        )


    @fixture
    def chara_param_last_element(self) -> CharaParam:
        return CharaParam(
            b'unit207_01_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            40,
            0,
            0,
            1,
            -1,
            -1.0,
            1,
            27,
            115,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            116,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00',
             b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00',
             b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00',
             b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00'],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            DamageParam(
                700.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0.0,
                1.0,
                0,
                0.0,
                0,
                0.0,
                5.0,
                3.0,
                0,
                0,
                10,
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [0.5, 0.5, 1.5, 1.0, 1.0, 1.0, 1.2000000476837158, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0, 0, 0, 1, 1, 1, 1, 0]
            ),
            b'chr53_04_01_1.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'Test01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'CARTICK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'equip_dmy.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )



    def test_verify_datafield_pos(self):
        assert BasesDataCharaParam.verify_datafield_pos()


    def test_get_byte_size(self,
            chara_param_header: BasesDataCharaParamHeader,
            chara_param_last_element: CharaParam,
            ):
        assert chara_param_header.get_byte_size() == 0x40
        assert chara_param_last_element.get_byte_size() == 0x400


    def test_from_bytes(self,
            chara_param_header: BasesDataCharaParamHeader,
            chara_param_last_element: CharaParam,
            ):
        file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\charaparam.dat"
        with open(file_name, "rb") as file:
            raw = file.read()
            actual: BasesDataCharaParam = BasesDataCharaParam.from_bytes(raw)
            assert BasesDataCharaParam.verify_filler(actual)

        assert actual.header.get_byte_size() == 0x40
        assert actual.header == chara_param_header

        assert len(actual.chara_params.param_list) == 0x29
        assert actual.chara_params.param_list[-1].get_byte_size() == 0x400
        assert actual.chara_params.param_list[-1] == chara_param_last_element



class Test_CharaParam:
    @fixture
    def file_one(self) -> str:
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\actor\\actor\\@unit000_01_01\\@localdata\\charaparam.dat"
    

    @fixture
    def file_two(self) -> str:
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\actor\\actor\\@unit002_01_01\\@localdata\\charaparam.dat"


    @fixture
    def chara_param_file_one(self) -> CharaParam:
        return CharaParam(
            b'unit000_01_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            0,
            0,
            0,
            0,
            0,
            1.0,
            0,
            0,
            115,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            116,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [b'\x02\x00\x14\x00', b'\x00\x00\x15\x00', b'\x01\x00\x15\x00', b'\x02\x00\x15\x00',
             b'\x03\x00\x15\x00', b'\x06\x00\x15\x00', b'\x05\x00\x15\x00', b'\x07\x00\x15\x00',
             b'\x08\x00\x15\x00', b'\n\x00\x15\x00', b'\x04\x00\x15\x00', b'\t\x00\x15\x00',
             b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00'],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            DamageParam(
                100.0,
                0.0,
                1.0,
                0.0,
                2.0,
                0.0,
                1.0,
                0,
                1.0,
                0,
                2.0,
                5.0,
                3.0,
                0,
                0,
                10,
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ),
            b'chr01_01_03_1.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'C_P_Gene.dat\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'PataPon\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'equip_dmy.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )
    

    @fixture
    def chara_param_file_two(self) -> CharaParam:
        return CharaParam(
            b'unit002_01_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            2,
            2,
            0,
            0,
            2,
            1.0,
            0,
            2,
            115,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            116,
            0.0,
            0.0,
            0,
            b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [b'\x02\x00\x14\x00', b'\x00\x00\x15\x00', b'\x01\x00\x15\x00', b'\x02\x00\x15\x00',
             b'\x03\x00\x15\x00', b'\x06\x00\x15\x00', b'\x05\x00\x15\x00', b'\x07\x00\x15\x00',
             b'\x08\x00\x15\x00', b'\n\x00\x15\x00', b'\x04\x00\x15\x00', b'\t\x00\x15\x00',
             b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', b'\x00\x00\x00\x00'],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            DamageParam(
                100.0,
                0.0,
                6.0,
                0.0,
                2.0,
                0.0,
                1.0,
                0,
                3.0,
                0,
                6.0,
                5.0,
                3.0,
                4,
                4,
                10,
                [0.10000000149011612, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                [1.0, 1.0, 0.800000011920929, 0.800000011920929, 0.5, 1.0, 1.2000000476837158, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ),
            b'chr01_01_02_1.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'C_P_Yumi.dat\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'YumiPon\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'equip_dmy.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )


    def test_verify_datafield_pos(self):
        assert CharaParam.verify_datafield_pos()


    def test_from_bytes_file_one(self,
            file_one: str,
            chara_param_file_one: CharaParam
            ):
        with open(file_one, "rb") as file:
            raw = file.read()
            actual: CharaParam = CharaParam.from_bytes(raw)
            assert CharaParam.verify_filler(actual)

        assert actual.get_byte_size() == 0x400
        assert actual == chara_param_file_one

    
    def test_from_bytes_file_two(self,
            file_two: str,
            chara_param_file_two: CharaParam
            ):
        with open(file_two, "rb") as file:
            raw = file.read()
            actual: CharaParam = CharaParam.from_bytes(raw)
            assert CharaParam.verify_filler(actual)

        assert actual.get_byte_size() == 0x400
        assert actual == chara_param_file_two