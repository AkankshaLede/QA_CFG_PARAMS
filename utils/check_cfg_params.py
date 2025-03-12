import configparser
import argparse

def read_cfg_to_dict(file_path):
    """Reads a .cfg file and converts it to a dictionary."""
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}

def validate_config(actual_cfg, expected_cfg, file1_cfg_path, file2_cfg_path):
    """Compares actual (A.cfg) and expected (B.cfg) configurations and prints mismatches."""
    mismatches = []
    flag = 0  # Default flag is 0 (graceful execution)

    # Check for ANY field marked as 'SHOULD_NOT_BE_PRESENT' in file2.cfg
    for section, expected_params in expected_cfg.items():
        for key, expected_value in expected_params.items():
            if expected_value == "SHOULD_NOT_BE_PRESENT":
                if section in actual_cfg and key in actual_cfg[section]:
                    mismatches.append(f"Error: '{key}' should not be present in section [{section}] in {file1_cfg_path}")
                    flag = 1

    # Standard comparison for other parameters
    for section, expected_params in expected_cfg.items():
        if section in actual_cfg:
            for key, expected_value in expected_params.items():
                if expected_value == "SHOULD_NOT_BE_PRESENT":
                    continue  # Skip as this is handled above

                actual_value = actual_cfg[section].get(key)
                if actual_value is None:
                    mismatches.append(f"{key} is missing in section [{section}] {file1_cfg_path}")
                elif actual_value != expected_value:
                    mismatches.append(f"{key} in section [{section}] is {actual_value}, expected {expected_value}")
        else:
            # skip if the entire section has ONLY `SHOULD_NOT_BE_PRESENT` fields
            if all(value == "SHOULD_NOT_BE_PRESENT" for value in expected_params.values()):
                continue
            mismatches.append(f"Section [{section}] is missing in {file1_cfg_path}")
    
    return mismatches, flag

#  Use argparse to take file paths as arguments
parser = argparse.ArgumentParser(description="Compare two .cfg files")
parser.add_argument('file1', type=str, help="Path to the first .cfg file")
parser.add_argument('file2', type=str, help="Path to the second .cfg file")

# Parse the arguments
args = parser.parse_args()

# Read configurations
actual_config = read_cfg_to_dict(args.file1)
expected_config = read_cfg_to_dict(args.file2)

# Validate configuration
mismatch_list, flag = validate_config(actual_config, expected_config, args.file1, args.file2)

# print mismatches
if mismatch_list:
    print("\n".join(mismatch_list))
else:
    print("All parameters match.")

print("Execution flag:", flag)
