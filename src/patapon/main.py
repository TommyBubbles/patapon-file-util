import sys
sys.path.insert(0, ".\\src")
# from patapon.filedata.p1.systemdata.itemtable_pac import ItemTable
# from patapon.filedata.p2.itemtable_pac import ItemTable
# from patapon.filedata.p2.itemmessage_msg import ItemMessage

# item_table_file_path = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@scriptlist\\itemtable.pac"
# # item_table_file_path = "D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@systemdata\\@systemdata\\@loadinggroupcmn\\@scriptlist\\itemtable.pac"
# with open(item_table_file_path, "rb") as file:
#     raw = file.read()
#     item_table: ItemTable = ItemTable.from_bytes(raw)


# item_msg_file_path = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemlocalizedata\\@default\\@localize\\@us\\@scriptlist\\itemmessage.msg"
# # item_msg_file_path = "D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@systemlocalizedata\\@localize\\@us\\@us\\@scriptlist\\itemmessage.msg"
# with open(item_msg_file_path, "rb") as file:
#     raw = file.read()
#     item_messages_obj: ItemMessage = ItemMessage.from_bytes(raw)


# with open("..\\item_dump_p1.txt", "w") as file:
#     for item in item_table.itemParamList.param_list:
#         pass
#         # print(item.id, item.iconModelName, item.modelName, item_messages_obj.find_message_by_index(item.nameId), item_messages_obj.find_message_by_index(item.explainId))
#         # file.write(f"{item.id}\t{item_messages_obj.find_message_by_index(item.nameId)}\n")
#         # print(item.id)
#         # print(f"{item_messages_obj.find_message_by_index(item.nameId)}")

# with open("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\@colony_msg\\@colony_msg\\@us\\colonymsg.pac", "rb") as file:
#     raw = file.read()
#     messages_obj: ItemMessage = ItemMessage.from_bytes(raw)
#     for message in messages_obj.item_messages.message_list:
#         print(message.message)

# import yaml
# with open("D:\\Patapon\\Patapon 1+2 Replay\\Patapon_Replay_Dump Project\\ExportedProject\\Assets\\AddressableMediaData\\P2\\Pac\\actor\\chara\\equip\\mission\\missionid_10340.bnd\\missiondata.bnd\\missionscript.asset", 'r') as file:
#     print(file.readline(), file.readline(), file.readline())

#     test = yaml.safe_load(file)
    
#     new_file_contents = bytes.fromhex(test["MonoBehaviour"]["bytes"])

#     with open(".\\replay_missionscript.pac", "wb") as output:
#         output.write(new_file_contents)


from patapon.filedata.p1.bnd import BND

def print_files(bnd: BND, path: str = "/"):
    file_info = bnd.header.get_ordered_linked_info('partition', 'dataOffset')
    partitions = bnd.partitions
    for i in range(bnd.header.nFiles):
        filename = file_info[i][1].name
        cur_partition = partitions[i]

        print(f"{cur_partition.__class__.__name__:<32}", path + filename)
        if type(cur_partition) == BND:
            print_files(cur_partition, path + filename + '/')

# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\paramlist.bnd"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@actorresourcenode\\@s_a_actor\\localdata.bnd"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@actorresourcenode\\@s_a_actor\\collisionparamlist.bnd"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@actorresourcenode\\@s_a_actor\\model.amdl"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@actorresourcenode\\s_a_actor.arc"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\actorresourcenode.bnd"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\layoutlist.layl"
filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\modellist.bnd"
with open(filepath, "rb") as file:
    raw = file.read()
    test: BND = BND.from_bytes(raw)
    print(test.header)
    print(f"header size: {hex(test.header.get_byte_size())}")
    print_files(test)
        
from patapon.filedata.p1.gxx import Gxx

# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@actorresourcenode\\@s_a_actor\\@model\\chr_dmy.gxx"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@modellist\\@loading\\nowloading.gxx"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@modellist\\@loading\\tips_now.gxx"
# filepath = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@modellist\\@loading\\tips_push.gxx"
# with open(filepath, 'rb') as file:
#     offset = 0
#     raw = file.read()
#     test: Gxx = Gxx.from_bytes(raw)
#     print(test.header)
#     offset += test.header.get_byte_size()
    
#     print(f"\nVertex Offset: {hex(offset)}\n")
#     for i in test.vertex_section.vertex_info:
#         print(i)
#         offset += i.get_byte_size()

#     print(f"\nMotion Command Offset: {hex(offset)}\n")
#     for i in test.motion_commands_section.command_sections:
#         print(i)
#         offset += i.get_byte_size()

#     print(f"\nMesh Header Offset: {hex(offset)}\n")
#     print(test.mesh_section.mesh_header)
#     offset += test.mesh_section.mesh_header.get_byte_size()
    
#     print(f"\nMesh Texture Pointers Offset: {hex(offset)}\n")
#     print(test.mesh_section.texture_pointers)
#     offset += test.mesh_section.texture_pointers.get_byte_size()

#     print(f"\nMotion Info Table Offset: {hex(offset)}\n")
#     print(test.mesh_section.motion_info_table)
#     offset += test.mesh_section.motion_info_table.get_byte_size()

#     print(f"\nBone Names Offset: {hex(offset)}\n")
#     print(test.mesh_section.bone_names)
#     offset += test.mesh_section.bone_names.get_byte_size()

#     print(f"\nTexture Info Offset: {hex(offset)}\n")
#     print(test.mesh_section.texture_list)
#     offset += test.mesh_section.texture_list.get_byte_size()

#     print(f"\nPadding Offset: {hex(offset)}\n")
#     print(test.mesh_section.padding)
#     offset += len(test.mesh_section.padding)

#     print(f"\nFile Size: {hex(offset)}\n")


# import gzip

# with gzip.open('D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\basesdata.bnd', 'rb') as file:
#     file_contents = file.read(0x25a7d8)
#     print(file_contents[:0x4])