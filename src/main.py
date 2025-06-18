# with open(".\\test\\files\\@unit010_01_01\\actorparam.dat", "rb") as file:
#     raw = file.read()
#     test_class = ActorParam.from_bytes(raw)
#     print(ActorParam.verify_filler(test_class))


# with open(".\\test\\files\\@unit010_01_01\\charaparam.dat", "rb") as file:
#     raw = file.read()
#     test_class = CharaParam.from_bytes(raw)
#     print(CharaParam.verify_filler(test_class))


# with open(".\\test\\files\\@unit010_01_01\\@collisionparamlist\\unit010_01_01_11.dat", "rb") as file:
#     raw = file.read()
#     test_class = CollisionParam.from_bytes(raw)
#     print(CollisionParam.verify_filler(test_class))


# with open(".\\test\\files\\@unit010_01_01\\@defaultequiplist\\unit010_01_01_22.dat", "rb") as file:
#     raw = file.read()
#     test_class = DefaultEquip.from_bytes(raw)
#     print(DefaultEquip.verify_filler(test_class))


# with open(".\\test\\files\\@unit010_01_01\\@nodenamelist\\unit010_01_01_h.dat", "rb") as file:
#     raw = file.read()
#     test_class = NodeNameParam.from_bytes(raw)
#     print(NodeNameParam.verify_filler(test_class))


# with open(".\\test\\files\\@egg001_01\\@model\\gimc620.gxt", "rb") as file:
#     raw = file.read()
#     test_class = GXT.from_bytes(raw)
#     print(GXT.verify_filler(test_class))
    
#     if isinstance(test_class, GXT):
#         print(test_class.decompressed_image())