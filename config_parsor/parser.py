import configparser

def read_cfg_to_dict(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    cfg_dict = {section: dict(config.items(section)) for section in config.sections()}
    return cfg_dict

# Example usage
file_a_dict = read_cfg_to_dict("A.cfg")
file_b_dict = read_cfg_to_dict("B.cfg")

print("A.cfg as dict:", file_a_dict)
print("B.cfg as dict:", file_b_dict)


print("-----------------------------------------------------------------------------------")
print("using basic file : ")
with open("A.cfg", "r") as f:
    print("A.cfg content:")
    print(f.read())

