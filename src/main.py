from filedata.equip_param import EquipParam

with open("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\equip\\@hlm003_05\\equipparam.dat", "rb") as file:
    raw = file.read()
    test_class = EquipParam.from_bytes(raw)
    print(EquipParam.verify_filler(test_class))