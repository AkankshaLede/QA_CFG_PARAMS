# # Read A.cfg
# a_cfg = {}
# with open("A.cfg", "r") as f:
#     section = None
#     for line in f:
#         line = line.strip()
#         if not line or line.startswith("#") or line.startswith(";"):  # Skip comments/empty lines
#             continue
#         if line.startswith("[") and line.endswith("]"):  # Section header
#             section = line[1:-1]
#             a_cfg[section] = {}
#         elif "=" in line and section:  # Key-value pair
#             key, value = line.split("=", 1)
#             a_cfg[section][key.strip()] = value.strip()

# # Read B.cfg
# b_cfg = {}
# with open("B.cfg", "r") as f:
#     section = None
#     for line in f:
#         line = line.strip()
#         if not line or line.startswith("#") or line.startswith(";"):
#             continue
#         if line.startswith("[") and line.endswith("]"):  
#             section = line[1:-1]
#             b_cfg[section] = {}
#         elif "=" in line and section:
#             key, value = line.split("=", 1)
#             b_cfg[section][key.strip()] = value.strip()

# # Debug: Print parsed dictionaries
# print("Parsed A.cfg:", a_cfg)
# print("Parsed B.cfg:", b_cfg)

# # Compare A.cfg and B.cfg
# mismatches_found = False

# for section in b_cfg:
#     if section in a_cfg:
#         for key in b_cfg[section]:
#             if key in a_cfg[section]:
#                 if a_cfg[section][key] != b_cfg[section][key]:
#                     print(f"Mismcatch: {key} in setion [{section}] is {a_cfg[section][key]}, expected {b_cfg[section][key]}")
#                     mismatches_found = True
#             else:
#                 print(f"Missing: {key} in section [{section}] of A.cfg")
#                 mismatches_found = True
#     else:
#         print(f"Missing section: [{section}] in A.cfg")
#         mismatches_found = True

# if not mismatches_found:
#     print("All parameters matched")




# import configparser

# def read_cfg_to_dict(file_path):
#     """Reads a .cfg file and converts it to a dictionary."""
#     config = configparser.ConfigParser()
#     config.read(file_path)
    
#     return {section: dict(config.items(section)) for section in config.sections()}

# def validate_config(actual_cfg, expected_cfg,file1_cfg_path,file2_cfg_path):
#     """Compares actual (A.cfg) and expected (B.cfg) configurations and prints mismatches."""
#     mismatches = []

#     for section, expected_params in expected_cfg.items():
#         if section in actual_cfg:
#             for key, expected_value in expected_params.items():
#                 actual_value = actual_cfg[section].get(key)
#                 if actual_value is None:
#                     mismatches.append(f"{key} is missing in section [{section}] {file1_cfg_path} ")
#                 elif actual_value != expected_value:
#                     mismatches.append(f"{key} in section [{section}] is {actual_value}, expected {expected_value}")
#         else:
#             mismatches.append(f"Section [{section}] is missing in A.cfg")

#     return mismatches

# # File paths
# file1_cfg_path = "A.cfg"
# file2_cfg_path = "B.cfg"


# # Read configurations
# actual_config = read_cfg_to_dict(file1_cfg_path)
# expected_config = read_cfg_to_dict(file2_cfg_path)

# print(actual_config)
# print(expected_config)

# # Validate
# mismatch_list = validate_config(actual_config, expected_config,file1_cfg_path,file2_cfg_path)

# # Print mismatches
# if mismatch_list:
#     print("\n".join(mismatch_list))
# else:
#     print("All parameters match.")




import configparser

def read_cfg_to_dict(file_path):
    """Reads a .cfg file and converts it to a dictionary."""
    config = configparser.ConfigParser()
    config.read(file_path)
    
    return {section: dict(config.items(section)) for section in config.sections()}

def validate_config(actual_cfg, expected_cfg, file1_cfg_path, file2_cfg_path):
    """Compares actual (A.cfg) and expected (B.cfg) configurations and prints mismatches."""
    mismatches = []
    flag = 0  # Default flag is 0 (graceful execution)
    
    # Check for system_type = SHOULD_NOT_BE_PRESENT case
    for section, expected_params in expected_cfg.items():
        if "system_type" in expected_params and expected_params["system_type"] == "SHOULD_NOT_BE_PRESENT":
            if "system_type" in actual_cfg.get(section, {}):
                # print("system_type should not be present, please remove it from", file1_cfg_path)
                flag = 1  # Set error flag
                
    for section, expected_params in expected_cfg.items():
        if section in actual_cfg:
            for key, expected_value in expected_params.items():
                actual_value = actual_cfg[section].get(key)
                if actual_value is None:
                    mismatches.append(f"{key} is missing in section [{section}] {file1_cfg_path}")
                elif actual_value != expected_value:
                    mismatches.append(f"{key} in section [{section}] is {actual_value}, expected {expected_value}")
        else:
            mismatches.append(f"Section [{section}] is missing in {file1_cfg_path}")
    
    return mismatches, flag

# Get file paths from user
file1_cfg_path = input("Enter the path of the first .cfg file: ")
file2_cfg_path = input("Enter the path of the second .cfg file: ")

# Read configurations
actual_config = read_cfg_to_dict(file1_cfg_path)
expected_config = read_cfg_to_dict(file2_cfg_path)

# Validate
mismatch_list, flag = validate_config(actual_config, expected_config, file1_cfg_path, file2_cfg_path)

# Print mismatches
if mismatch_list:
    print("\n".join(mismatch_list))
else:
    print("All parameters match.")

print("Execution flag:", flag)


# improvements : user input file name 
# not to have sysytem_type(print only now)
# after sometime flag for that(0 gracefully , system module , flag 1 = error)
# gitlab = fail pr 
# change files data also
# use : use argparser 


# import configparser
# import os

# def read_cfg_to_dict(file_path):
#     """Reads a .cfg file and converts it to a dictionary."""
#     config = configparser.ConfigParser()
#     config.read(file_path)
    
#     return {section: dict(config.items(section)) for section in config.sections()}

# def write_cfg_from_dict(file_path, config_dict):
#     """Writes a dictionary back to a .cfg file."""
#     config = configparser.ConfigParser()
#     for section, params in config_dict.items():
#         config[section] = params
#     with open(file_path, 'w') as configfile:
#         config.write(configfile)

# def validate_config(actual_cfg, expected_cfg, file1_cfg_path, file2_cfg_path):
#     """Compares actual (file1.cfg) and expected (file2.cfg) configurations and prints mismatches."""
#     mismatches = []
#     flag = 0  # Default flag is 0 (graceful execution)
    
#     modified = False  # Track if modifications are made
    
#     # Check for system_type = SHOULD_NOT_BE_PRESENT case
#     for section, expected_params in expected_cfg.items():
#         if "system_type" in expected_params and expected_params["system_type"] == "SHOULD_NOT_BE_PRESENT":
#             if "system_type" in actual_cfg.get(section, {}):
#                 print("system_type should not be present, removing it from", file1_cfg_path)
#                 del actual_cfg[section]["system_type"]  # Remove system_type
#                 modified = True
#                 flag = 1  # Set error flag
    
#     # Save changes if modifications were made
#     if modified:
#         write_cfg_from_dict(file1_cfg_path, actual_cfg)
    
#     for section, expected_params in expected_cfg.items():
#         if section in actual_cfg:
#             for key, expected_value in expected_params.items():
#                 actual_value = actual_cfg[section].get(key)
#                 if actual_value is None:
#                     mismatches.append(f"{key} is missing in section [{section}] {file1_cfg_path}")
#                 elif actual_value != expected_value:
#                     mismatches.append(f"{key} in section [{section}] is {actual_value}, expected {expected_value}")
#         else:
#             mismatches.append(f"Section [{section}] is missing in {file1_cfg_path}")
    
#     return mismatches, flag

# # Get file paths from user
# file1_cfg_path = input("Enter the path of the first .cfg file: ")
# file2_cfg_path = input("Enter the path of the second .cfg file: ")

# # Check if files exist
# if not os.path.isfile(file1_cfg_path):
#     print("Error: The first file does not exist. Please enter a correct file name.")
#     exit(1)
# if not os.path.isfile(file2_cfg_path):
#     print("Error: The second file does not exist. Please enter a correct file name.")
#     exit(1)

# # Read configurations
# actual_config = read_cfg_to_dict(file1_cfg_path)
# expected_config = read_cfg_to_dict(file2_cfg_path)

# # Validate
# mismatch_list, flag = validate_config(actual_config, expected_config, file1_cfg_path, file2_cfg_path)

# # Print mismatches
# if mismatch_list:
#     print("\n".join(mismatch_list))
# else:
#     print("All parameters match.")

# print("Execution flag:", flag)
