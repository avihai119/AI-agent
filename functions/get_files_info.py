import os

from google.genai import types 

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        abs_pwd_path = os.path.abspath(working_directory)
        path_to_target_dir = os.path.normpath(os.path.join(abs_pwd_path, directory))
        valid_target_dir = os.path.commonpath([abs_pwd_path, path_to_target_dir]) == abs_pwd_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        if not os.path.isdir(path_to_target_dir):
            return f'Error: "{directory}" is not a directory\n'
    
        target_dir_list = os.listdir(path_to_target_dir)
        target_dir_data = ""

        for item in target_dir_list:
            full_path = os.path.join(path_to_target_dir, item)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path)
            target_dir_data += f"   - {item}: file_size={size} bytes, is_dir={is_dir}\n"

        return target_dir_data
    except Exception as e:
        return f'Error reading directory "{directory}": {e}'
