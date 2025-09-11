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



# from hashlib import sha1, md5


# with open('D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\abnormalstatusparam.dat', 'rb') as file:
#     raw = file.read()
#     sha1_hash = sha1(raw)
#     md5_hash = md5(raw)
#     print(sha1_hash.hexdigest())
#     print(md5_hash.hexdigest())
#     print(hex(0x08584955))



from patapon.filedata.p1.bnd import BND


with open("D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\DATA_CMN.BND", "rb") as file:
    raw = file.read()
    test: BND = BND.from_bytes(raw)
    print(test.header)
    print(len(test.partition_info.info_list))
    for i in test.partition_info.info_list:
        print(i)