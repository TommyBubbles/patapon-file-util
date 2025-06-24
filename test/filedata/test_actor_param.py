import sys
sys.path.insert(0, ".\\src")
from patapon.filedata import ActorParam


def test_verify_datafield_pos_actor_param():
    assert ActorParam.verify_datafield_pos()


def test_from_bytes_actor_param_file_one():
    file_name = ".\\test\\files\\@unit010_01_01\\actorparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = ActorParam.from_bytes(raw)
        assert ActorParam.verify_filler(actual)

    expected = ActorParam(
        "ActorChara",
        0x0,
        [0,0,0],
        "0",
        0x1A,
        [0,0,0,0,0,0,0],
        "none",
        "none",
        "none",
        "none",
        "none",
        "none",
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "none",
        "none",
        "none",
        "none"
    )

    assert actual == expected