import configparser


def read_cfg_to_dict(file_path):
    """Reads a .cfg file and converts it to a dictionary"""
    config = configparser.ConfigParser()
    config.read(file_path)

    for section in config.sections():
        print({section:dict(config.items(section))})


file1_cfg_path = input("enter the path of the first .cfg file: ")
file2_cfg_path = input("enter the path of the second .cfg file: ")

actual_config = read_cfg_to_dict(file1_cfg_path)
expected_config = read_cfg_to_dict(file2_cfg_path)
