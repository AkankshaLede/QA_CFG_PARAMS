a_cfg = {}
with open("A.cfg", "r") as f:
    for i in f:
        i = i.strip()
        if not i or "=" not in i:
            continue
        key,value = i.split("=",1)
        a_cfg[key.strip()] = a_cfg.get(key.strip(),value.strip())


b_cfg = {}
with open("B.cfg", "r") as f:
    for i in f:
        i = i.strip()
        if not i or i.startswith("#") or i.startswith(";"):
            continue
        if "=" in i:
            key,value = i.split("=",1)
            b_cfg[key.strip()] = b_cfg.get(key.strip(),value.strip())


print("A.cfg : ",a_cfg)
print("B.cfg : ",b_cfg)

mismatches_found = False

mismatches_found = False

for key in b_cfg:
    if key in a_cfg:
        if a_cfg[key] != b_cfg[key]:
            print(f"Mismatch: {key} is {a_cfg[key]}, expected {b_cfg[key]}")
            print(f"{key} is not matching")
            mismatches_found = True
    else:
        print(f"Missing: {key} in A.cfg")
        mismatches_found = True

if not mismatches_found:
    print("All parameters match!")
