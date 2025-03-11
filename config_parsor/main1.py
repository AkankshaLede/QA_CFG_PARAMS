# import configparser

# def read_cfg_to_dict(file_path):
#     config = configparser.ConfigParser()
#     config.read(file_path)
    
#     cfg_dict = {section: dict(config.items(section)) for section in config.sections()}
#     return cfg_dict

# # Example usage
# file_a_dict = read_cfg_to_dict("A.cfg")
# file_b_dict = read_cfg_to_dict("B.cfg")

# print("A.cfg as dict:", file_a_dict)
# print("B.cfg as dict:", file_b_dict)


a_cfg = {}
with open("A.cfg", "r") as f:
    for i in f:
        i = i.strip()  # Remove leading/trailing spaces and newlines
        if not i or "=" not in i:  # Skip empty lines or lines without '='
            continue
        key, value = i.split("=", 1) 
        a_cfg[key.strip()] = a_cfg.get(key.strip(), value.strip())

    # for line in f:
    #     line = line.strip()
    #     if not line or line.startswith("#") or line.startswith(";"):  # Skip empty lines and comments
    #         continue
    #     if "=" in line:  # Key-value pair
    #         key, value = line.split("=", 1)
    #         a_cfg[key.strip()] = value.strip()


b_cfg = {}
with open("B.cfg", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            b_cfg[key.strip()] = value.strip()

print("Parsed A.cfg:", a_cfg)
print("Parsed B.cfg:", b_cfg)


mismatches_found = False

for key in b_cfg:
    if key in a_cfg:
        if a_cfg[key] != b_cfg[key]:
            print(f"Mismatch: {key} is {a_cfg[key]}, expected {b_cfg[key]} it is not matching ")
            mismatches_found = True
    else:
        print(f"Missing: {key} in A.cfg")
        mismatches_found = True

if not mismatches_found:
    print("All parameters match!")



