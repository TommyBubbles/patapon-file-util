from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.windpath import (
    WindPath,
    WindPathHeader,
    WindPathInfo,
    WindPathNode,
    WindPathVector
)
from patapon.filedata.patapon_data_class import PataponDataIO



class Test_FileOne:
    @fixture
    def filepath(self):
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@windpath\\unknown_0.bnd"


    @fixture
    def windpath_header(self) -> WindPathHeader:
        return WindPathHeader(
            b'Path',
            0,
            [0, 0, 0],
            1,
            [
                WindPathInfo(
                    0,
                    4,
                    64,
                    877.7215576171875,
                    b'LINE01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode()
                )
            ],
            0,
        )


    @fixture
    def windpath_node_last_element(self) -> WindPathNode:
        return WindPathNode(
            WindPathVector(
                400.2889099121094,
                85.41759490966797,
                -5.820212209073361e-06,
                1.0,
            ),
            WindPathVector(
                307.886962890625,
                54.643798828125,
                -3.9859505704953335e-06,
                1.0
            ),
            WindPathVector(
                492.6908264160156,
                116.19139099121094,
                -7.654472938156687e-06,
                1.0
            ),
            0.0,
            [0, 0, 0],
        )



    def test_verify_datafield_pos(self):
        assert WindPath.verify_datafield_pos()


    def test_get_byte_size(self,
            windpath_header: WindPathHeader,
            windpath_node_last_element: WindPathNode
            ):
        assert windpath_header.get_byte_size() == 0x40
        assert windpath_node_last_element.get_byte_size() == 0x40


    def test_from_bytes(self,
                        filepath: str,
            windpath_header: WindPathHeader,
            windpath_node_last_element: WindPathNode
            ):
        with open(filepath, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: WindPath = WindPath.from_bytes(data_stream)
            assert WindPath.verify_filler(actual)

        assert actual.get_byte_size() == 0x140

        assert actual.header.get_byte_size() == 0x40
        assert actual.header == windpath_header

        assert len(actual.windpaths.windpath_nodes) == 4
        assert actual.windpaths.windpath_nodes[-1].get_byte_size() == 0x40
        assert actual.windpaths.windpath_nodes[-1] == windpath_node_last_element
