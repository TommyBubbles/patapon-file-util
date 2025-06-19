import sys
sys.path.insert(0, ".\\src")
from patapon.filedata import NodeNameParam


def test_verify_datafield_pos_node_name_param():
    assert NodeNameParam.verify_datafield_pos()


def test_from_bytes_node_name_param_file_one():
    file_name = ".\\test\\files\\@unit010_01_01\\@nodenamelist\\unit010_01_01_h.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = NodeNameParam.from_bytes(raw)
        assert NodeNameParam.verify_filler(actual)

    expected = NodeNameParam(
        "unit010_01_01_H",
        0x54,
        [0,0,0],
        0xC,
        1,
        [0,0],
        "0",
        "0",
        "none",
        "unit010_01_01_H",
        "helm",
        "0"
    )

    assert actual == expected