import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p2 import CharaParam


def test_verify_datafield_pos_chara_param():
    assert CharaParam.verify_datafield_pos()


def test_from_bytes_chara_param_file_one_from_bytes():
    file_name = ".\\test\\files\\@unit010_01_01\\charaparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = CharaParam.from_bytes(raw)
        assert CharaParam.verify_filler(actual)

    expected = CharaParam(
        "unit010_01_01",
        0xB,
        0xC,
        0x8,
        0x0,
        0xA,
        1.0,
        0x0,
        0xA,
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        11.0,
        [0,0],
        0,
        1,
        0,
        0,
        "0",
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "chr01_01_10_1.amdl",
        "C_P_Hohei.dat",
        "ロボポン",
        "",
        "stnd009.amdl",
        "0",
        "0",
        [0,0,0,0,0,0,0,0],
        "0",
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    )

    print(actual)
    print(expected)
    assert actual == expected