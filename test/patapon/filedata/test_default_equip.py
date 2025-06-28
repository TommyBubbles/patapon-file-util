import sys
sys.path.insert(0, ".\\src")
from patapon.filedata import DefaultEquip


def test_verify_datafield_pos_default_equip_param():
    assert DefaultEquip.verify_datafield_pos()


def test_from_bytes_default_equip_param_file_one():
    file_name = ".\\test\\files\\@unit010_01_01\\@defaultequiplist\\unit010_01_01_22.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = DefaultEquip.from_bytes(raw)
        assert DefaultEquip.verify_filler(actual)
        
    expected = DefaultEquip(
        "unit010_01_01_22",
        0x16,
        [0,0,0,0],
        0x0,
        [0,0],
        "0",
        "0",
        "none",
        "wpn010_001_01",
        "0",
        "0"
    )

    assert actual == expected