from filedata import *

with open("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\equip\\@hlm003_05\\equipparam.dat", "rb") as file:
    raw = file.read()
    test_class = EquipParam.from_bytes(raw)
    print(EquipParam.verify_filler(test_class))


with open("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\equip\\@hlm003_06\\actorparam.dat", "rb") as file:
    raw = file.read()
    test_class = ActorParam.from_bytes(raw)
    print(ActorParam.verify_filler(test_class))


with open("d:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\chara\\@unit002_01_01\\charaparam.dat", "rb") as file:
    raw = file.read()
    test_class = CharaParam.from_bytes(raw)
    print(CharaParam.verify_filler(test_class))