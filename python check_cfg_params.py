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

