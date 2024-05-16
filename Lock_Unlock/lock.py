import os

def lock_files_and_folders(directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            # Remove all permissions for directories
            os.chmod(dir_path, 0)
            # Hide directories by renaming them
            os.rename(dir_path, os.path.join(root, '.' + name))
        for name in files:
            file_path = os.path.join(root, name)
            # Remove all permissions for files
            os.chmod(file_path, 0)
            # Hide files by renaming them
            os.rename(file_path, os.path.join(root, '.' + name))

# Construct the output path
output_path = os.path.join(os.getcwd(), 'Lock_Unlock', 'Lock')

# Call the function to lock files and folders
lock_files_and_folders(output_path)
# Rename the 'Lock' directory to hide it
os.rename(output_path, os.path.join(os.getcwd(), 'Lock_Unlock', '.' + 'Lock'))

