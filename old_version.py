import os
import shutil
from pathlib import Path
import platform


def get_our_precious_time(file_path):
    info = file_path.stat().st_mtime
    return info


if platform.system() == 'Linux':
    Reverse_Solidus = "/ "
else:
    Reverse_Solidus = "\ "

print("Pls write directories paths")
tree1 = input()
tree2 = input()
print("Pls, choose option")
print(f"2 - Copy contents of {tree1} to {tree2}"
      f"\n3 - Copy contents of {tree2} to {tree1}")

chosen_option = input()
while chosen_option not in ['2', '3']:
    print("Pls, choose an option which does exist")
    print(f"2 - Copy contents of {tree1} to {tree2}"
          f"\n3 - Copy contents of {tree2} to {tree1}")

    chosen_option = input()

if chosen_option == '2':
    des_tree = tree2
    str_tree = tree1
else:
    des_tree = tree1
    str_tree = tree2

current_dir = Path(des_tree)
for des_path in current_dir.iterdir():
    filename = des_path.name
    str_path = str_tree + Reverse_Solidus[0] + filename
    if os.path.isfile(str_path):
        print(filename)
        time_des = get_our_precious_time(des_path)
        time_str = get_our_precious_time(Path(str_path))
        if time_str > time_des:
            shutil.copy(str_path, des_path.absolute())
            print("was changed")
