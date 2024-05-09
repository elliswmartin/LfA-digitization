import os
from tqdm import tqdm
from datetime import datetime
from pathlib import Path

def document_files(server_path, output_file):
    """Document every file in the folder structure."""
    with open(output_file, 'w') as f:
        f.write("List of Files:\n")
        file_count = 0
        for root, dirs, files in tqdm(os.walk(server_path), desc="Processing", unit="folders"):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(file_path + "\n")
                file_count += 1
    print(f"Total files processed: {file_count}")

def get_dated_dir_path(base_path, prefix="dirs"):
    """Create and return a path with prefix-YYMMDD format inside base_path."""
    # Get today's date in YYMMDD format
    date_str = datetime.now().strftime("%y%m%d")
    # New folder name with "prefix-YYMMDD" format
    new_folder_name = f"{prefix}-{date_str}"
    # Path for the new folder
    new_path = os.path.join(base_path, new_folder_name)
    # Create the new folder if it doesn't exist
    os.makedirs(new_path, exist_ok=True)
    return new_path

if __name__ == "__main__":
    # Create dated folder paths
    desktop_base = os.path.join(Path.home(), "Desktop")    
    output_folder_path = get_dated_dir_path(desktop_base)

    # # Server
    # server_path = "/Volumes/Shared"
    # output_file = os.path.join(output_folder_path, "server_directory.txt")
    # document_files(server_path, output_file)
    # print("File list documented. Check '{}' for output.".format(output_file))

    # # Promise 1
    # p1_path = r"/Volumes/Promise Pegasus"
    # output_file = os.path.join(output_folder_path, "promise1_directory.txt")
    # document_files(p1_path, output_file)
    # print("File list documented. Check '{}' for output.".format(output_file))

    # # Promise 2
    # p2_path = r"/Volumes/Promise Pegasus 2"
    # output_file = os.path.join(output_folder_path, "promise2_directory.txt")
    # document_files(p2_path, output_file)
    # print("File list documented. Check '{}' for output.".format(output_file))

    # Ellis-LfA
    ellis_path = "/Volumes/Ellis-LfA"
    output_file = os.path.join(output_folder_path, "ellis_directory.txt")
    document_files(ellis_path, output_file)
    print("File list documented. Check '{}' for output.".format(output_file))