
# the idea for setting up the ids for each instruction and how to extract it from the class
# import sys
# sys.path.insert(0, ".\\src")
# from patapon.filedata.pac_inst import group_00


# for i in group_00.__dict__.keys():
#     value = group_00.__dict__[i]
#     if i.startswith("PacInstruction") and \
#             issubclass(value, group_00.PacInstruction) and \
#             value is not group_00.PacInstruction:
#         print(i, value.id)