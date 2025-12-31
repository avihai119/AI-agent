import os

def write_file(working_directory, file_path, content):
    try:
        abs_pwd_path = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(abs_pwd_path, file_path))
        valid_target_file = os.path.commonpath([abs_pwd_path, path_to_target_file]) == abs_pwd_path

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path_to_target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(path_to_target_file)
        os.makedirs(parent_dir, exist_ok=True)
        
        with open(path_to_target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: writing to file "{file_path}": {e}'
