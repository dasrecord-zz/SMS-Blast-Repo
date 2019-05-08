import json
from vip import vip as vip
print(vip)
def add_vip():
    # existing = f.read()
    # print(artists)
    while True:
        f = open('vip.py', 'w')
        name = input("Add Name:   ")
        if str(name) == "quit":
            f.write("vip = ")
            f.write(str(vip))
            f.close()
            return False
        else:
            cell = input("Add Number:   ")
            vip[name] = cell
            print(vip)
            f.write("vip = ")
            f.write(str(artists))
            f.close()
add_vip()

# with open("artists.json") as f:
    # ACCESS DATA AS JSON OBJECT
    # content = f.read()
    # print(type(content))
    # print(content)

    # ACCESS DATA AS PYTHON OBJECT
    # content = json.load(f)
    # print(content)
    # print(type(content))
    # f.close()
