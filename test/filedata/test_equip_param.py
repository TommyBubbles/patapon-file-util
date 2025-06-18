import sys
sys.path.insert(0, ".\\src")
from patapon.filedata import EquipParam


def test_equip_param_file_one_from_bytes():
    with open(".\\test\\files\\@hlm001_01\\equipparam.dat", "rb") as file:
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