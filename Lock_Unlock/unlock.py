import os

def unlock_files_and_folders(directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            # Restore original permissions for directories
            os.chmod(dir_path, 0o755)  # Adjust permissions according to your needs
            # Unhide directories by renaming them back
            os.rename(dir_path, os.path.join(root, name.lstrip('.')))
        for name in files:
            file_path = os.path.join(root, name)
            # Restore original permissions for files
            os.chmod(file_path, 0o644)  # Adjust permissions according to your needs
            # Unhide files by renaming them back
            os.rename(file_path, os.path.join(root, name.lstrip('.')))

# Construct the output path
output_path = os.path.join(os.getcwd(), 'Lock_Unlock', '.' + 'Lock')

# Call the function to unlock files and folders
unlock_files_and_folders(output_path)

# Corrected the final os.rename call
os.rename(output_path, os.path.join(os.getcwd(), 'Lock_Unlock', 'Lock'))
