import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p2 import EquipParam


def test_verify_datafield_pos_equip_param():
    assert EquipParam.verify_datafield_pos()


def test_from_bytes_equip_param_file_one():
    file_name = ".\\test\\files\\@hlm001_01\\equipparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = EquipParam.from_bytes(raw)
        assert EquipParam.verify_filler(actual)

    expected = EquipParam(
        "hlm001_01",
        0x24B,
        [0,0,0,0],
        1,
        -1,
        0,
        -1,
        [0,0],
        -1,
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "hlm000_0_001.amdl",
        [0,0,0,0,0,0,0,0]
    )

    assert actual == expected