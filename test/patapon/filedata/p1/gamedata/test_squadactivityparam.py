import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.gamedata.squadactivityparam import SquadActivityParam


def test_verify_datafield_pos_actor_param():
    assert SquadActivityParam.verify_datafield_pos()


def test_from_bytes_actor_param_file_one():
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\squadactivityparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual = SquadActivityParam.from_bytes(raw)
        assert SquadActivityParam.verify_filler(actual)


    assert len(actual.base_param.param_list) == 0xD5
    assert len(actual.missile_param.param_list) == 0x1B