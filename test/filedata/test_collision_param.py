import sys
sys.path.insert(0, ".\\src")
from patapon.filedata import CollisionParam


def test_verify_datafield_pos_collision_param():
    assert CollisionParam.verify_datafield_pos()


def test_from_bytes_collision_param_file_one_from_bytes():
    file_name = ".\\test\\files\\@unit010_01_01\\@collisionparamlist\\unit010_01_01_11.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = CollisionParam.from_bytes(raw)
        assert CollisionParam.verify_filler(actual)

    expected = CollisionParam(
        "unit010_01_01_11",
        0xB,
        [0,0,0],
        10.0,
        10.0,
        0,
        2,
        "eye",
        "0"
    )

    print(actual)
    print(expected)
    assert actual == expected