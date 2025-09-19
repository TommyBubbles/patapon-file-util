from typing import Literal, Any
from collections import OrderedDict

def get_func_name(func_id: bytes, func_table: dict[bytes, dict]) -> str:
    if func_table.get(func_id, None) is None:
        return func_id.hex()
    return func_table[func_id]["func_name"]


def trim_offset(offset: int) -> str:
    hex_offset = offset.to_bytes(4, "big").hex()
    while hex_offset.find("0") == 0 and len(hex_offset) > 1:
        hex_offset = hex_offset.removeprefix("0")
    hex_offset = "0x" + hex_offset.upper()
    return hex_offset


def write_to_file(offset: int, func_id: bytes, func_params: list[bytes], func_table: dict[bytes,dict], output):
    hex_offset = trim_offset(offset)
    func_name = get_func_name(func_id, func_table)

    output.write(hex_offset)
    output.write("\t")
    output.write(func_name)
    output.write("\n")

    for param in func_params:
        output.write("\t")
        output.write(param.hex())
        output.write("\n")

    if func_name in ["cmd_end", "cmd_jmp"]:
        output.write("\n")


def pac_object(input_file_path: str, func_table: dict[bytes,dict], file_type: Literal["stage","mission"]) -> OrderedDict[str,list[dict]]:
    pac_funcs = OrderedDict()
    
    with open(input_file_path, "rb") as input_file:
        raw = input_file.read()

        if file_type == "stage":
            offset = int.from_bytes(raw[4:8], "little")
        else:
            offset = 0

        func_id = None
        prev_offset = offset
        func_params = []
        pac_commands = []
        while offset < len(raw):
            next = raw[offset:offset+4]
            # check for function id
            if next[0] == 0x25 and next[1] != b'\x00' and next[2:] != b'\x00\x00':
                if func_id is not None:
                    func_name = get_func_name(func_id, func_table)
                    str_offset = trim_offset(prev_offset)
                    pac_info = {
                        "offset": str_offset,
                        "func_id": func_id,
                        "func_name": func_name,
                        "params": func_params
                    }
                    pac_commands.append(pac_info)
                    func_params = []
                
                    # end of code section
                    if func_name in ["cmd_end", "cmd_jmp", "cmd_inxJmp"]:
                        start_offset = pac_commands[0]["offset"]
                        func_range = f"{start_offset} - {str_offset}"
                        pac_funcs[func_range] = pac_commands
                        pac_commands = []

                prev_offset = offset
                func_id = next
            else:
                if func_id == b'\x25\x10\x1C\x00':
                    func_params.append(next)
                    func_params.append(raw[offset+4:offset+8])
                    
                    i = 0
                    while raw[offset+8+i] != 0:
                        i += 1
                        print(raw[offset+8+i])
                    func_params.append(raw[offset+8:offset+8+i+4-(i%4)].decode("shift-jis"))
                    offset += 4 + i+4-(i%4)
                else:
                    func_params.append(next)

            offset += 4

        if func_id is not None and (get_func_name(func_id, func_table) == "cmd_end" or len(func_params) != 0):
            func_name = get_func_name(func_id, func_table)
            str_offset = trim_offset(offset)
            pac_info = {
                "offset": str_offset,
                "func_id": func_id,
                "func_name": func_name,
                "params": func_params
            }
            pac_commands.append(pac_info)
            start_offset = pac_commands[0]["offset"]
            func_range = f"{start_offset} - {str_offset}"
            pac_funcs[func_range] = pac_commands

    return pac_funcs
    

def get_mission_info(input_file_path: str) -> dict:
    results = {}
    
    with open(input_file_path, "rb") as input_file:
        raw_bytes = input_file.read()
        mission_id = raw_bytes[0:0x20].strip(b'\x00').decode()
        mission_index = int.from_bytes(raw_bytes[0x20:0x24], 'little')
        
        results = {
            "mission_id": mission_id,
            "mission_index": mission_index,
            "mission_index_hex": trim_offset(mission_index)
        }

    return results


def run_mission_dump():
    import os

    folder = "D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\mission"
    if os.path.isdir(folder) is False:
        return

    mission_info = []
    for file in os.listdir(folder):
        filepath = folder + os.sep + file + os.sep + "@missiondata" + os.sep + "missionparam.dat"
        if os.path.isfile(filepath) is False:
            continue
        info = get_mission_info(filepath)
        mission_info.append(info)
        print(info)
        
    output_file_path = "./mission_dump.txt"
    with open(output_file_path, "w") as output_file:
        for info in mission_info:
            output_file.write(f"{info['mission_id']}\t{info['mission_index']}\t{info['mission_index_hex']}\n")



def dump_pac(input_file_path: str, output_file_path: str, func_table: dict[bytes,dict], file_type: Literal["stage","mission"]):
    with open(output_file_path, "w") as output_file:
        with open(input_file_path, "rb") as input_file:
            raw = input_file.read()

            if file_type == "stage":
                offset = int.from_bytes(raw[4:8], "little")
            else:
                offset = 0

            func_id = None
            prev_offset: int = offset
            func_params = []
            while offset < len(raw):
                next = raw[offset:offset+4]
                # check for function id
                if next[0] == 0x25 and next[1] != b'\x00' and next[2:] != b'\x00\x00':
                    if func_id is not None:
                        write_to_file(prev_offset, func_id, func_params, func_table, output_file)
                        func_params = []
                    
                    prev_offset = offset
                    func_id = next
                else:
                    func_params.append(next)

                offset += 4

            if len(func_params) != 0 and func_id is not None:
                write_to_file(prev_offset, func_id, func_params, func_table, output_file)


def get_func_info():
    func_info = {}
    with open("D:\\Patapon\\Tools\\newest_p2_instruction_set.bin", "r") as func_file:
        for line in func_file.readlines():
            raw_func_info = line.split(";")
            func_info_id = b''
            
            func_info_id += bytes.fromhex(raw_func_info[0])
            func_name = raw_func_info[1]

            func_params = []
            for i in range(4, len(raw_func_info),2):
                param_info = {
                    "type": raw_func_info[i],
                    "name": raw_func_info[i+1]
                }
                func_params.append(param_info)

            func_info[func_info_id] = {
                "func_name": func_name,
                "params": func_params
            }
    return func_info


def run_dump():
    func_info = get_func_info()
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\march.pac", "march_dump.txt", func_info, 'mission')
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\gamemain.pac", "gamemain_dump.txt", func_info, 'mission')
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\missionmain.pac", "missionmain_dump.txt", func_info, 'mission')
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\unitbase.pac", "unitbase_dump.txt", func_info, 'mission')
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\unitsquad.pac", "unitsquad_dump.txt", func_info, 'mission')
    # dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\mission\\@missionid_10320\\@missiondata\\stagescript.pac", "pac_stage_dump.txt", func_info, 'stage')
    dump_pac("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\actor\\mission\\@missionid_10340\\@missiondata\\missionscript.pac", "pac_mission_dump.txt", func_info, 'mission')

from tkinter import *
from tkinter import ttk
from functools import partial

def display_pac_info(*args, output_frame: ttk.Frame | None = None, listbox: Listbox | None = None, pac_commands: list[dict] = []):
    if output_frame is not None and listbox is not None:
        selection = listbox.curselection()

        if len(selection) == 1:
            index = int(selection[0])
            command = pac_commands[index]

            old_contents = output_frame.winfo_children()
            for child in old_contents:
                child.destroy()

            func_params = command["params"]
            for i in range(0, len(func_params), 50):
                column_set = (i//50)
                column_value = ttk.Label(output_frame, text="Value")
                column_value.grid(column=1+2*column_set, row=0)

                
                for j in range(i, min(i + 50,len(func_params))):
                    param_label = ttk.Label(output_frame, text=f"Param {j+1}")
                    param_label.grid(column=2*column_set, row=(j%50)+1)


                    if type(func_params[j]) is str:
                        param_str = func_params[j]
                    else:
                        param_str = func_params[j].hex()

                    param_value = ttk.Label(output_frame, text=f"{param_str}")
                    param_value.grid(column=1+2*column_set, row=(j%50)+1)

        print(listbox.curselection())


def display_pac_func_commands(*args, output_frame: ttk.Frame | None = None, listbox: Listbox | None = None, pac_funcs: OrderedDict[str,list[dict]] = OrderedDict()):
    if output_frame is not None and listbox is not None:
        selection = listbox.curselection()

        if len(selection) == 1:
            index = int(selection[0])
            commands = list(pac_funcs.values())[index]

            old_contents = output_frame.winfo_children()
            for child in old_contents:
                child.destroy()

            command_listbox = Listbox(output_frame, height=5, width=30)
            command_listbox.grid(column=0, row=0, sticky=(N,E,S,W))

            command_scroll = ttk.Scrollbar(output_frame, orient=VERTICAL, command=command_listbox.yview)
            command_scroll.grid(column=1, row=0, sticky=(N,S))
            command_listbox["yscrollcommand"] = command_scroll.set

            param_frame = ttk.Frame(output_frame, padding=10)
            param_frame.grid(column=2, row=0, sticky=(N,E,S,W))


            for command in commands:
                command_listbox.insert('end', f'{command["offset"]}:{command["func_name"]}')

            apply_selection = partial(display_pac_info, output_frame=param_frame, listbox=command_listbox, pac_commands=commands)
            command_listbox.bind("<<ListboxSelect>>", apply_selection)

        print(listbox.curselection())

pac_funcs = pac_object("D:\\Patapon\\Patapon Stuff\\Patapon 2\\@DATA_CMN\\loadinggroup\\@gamedata\\@loadinggroupcmn\\@loadinggroupcmn\\@scriptlist\\unitbase.pac", get_func_info(), 'mission')

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

list_frame = ttk.Frame(frame, padding=10)
list_frame.grid(columnspan=1)

param_frame = ttk.Frame(frame, height=10)
param_frame.grid(column=1, row=0, sticky=(N,S))

main_list = Listbox(list_frame, height=5)
main_list.grid(column=0, row=0, sticky=(N,E,S,W))

apply_selection = partial(display_pac_func_commands, output_frame=param_frame, listbox=main_list, pac_funcs=pac_funcs)
main_list.bind("<<ListboxSelect>>", apply_selection)

main_scroll = ttk.Scrollbar(list_frame, orient=VERTICAL, command=main_list.yview)
main_scroll.grid(column=1, row=0, sticky=(N,S))
main_list["yscrollcommand"] = main_scroll.set

for offset in pac_funcs.keys():
    main_list.insert('end', f'{offset}')

ttk.Button(frame, text="Run Pac Dump", command=run_dump).grid(column=0, row=1)
ttk.Button(frame, text="Get Mission info", command=run_mission_dump).grid(column=1, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=2, row=1)

# centers the widgets
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()