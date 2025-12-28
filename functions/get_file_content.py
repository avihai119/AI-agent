import os

from config import *

def get_file_content(working_directory, file_path):
    try:
        abs_pwd_path = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(abs_pwd_path, file_path))
        valid_target_file = os.path.commonpath([abs_pwd_path, path_to_target_file]) == abs_pwd_path

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
        if not os.path.isfile(path_to_target_file):
            return f'Error: File is not found or is not not a regular file: "{file_path}"\n'
    
        with open(path_to_target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at MAX_CHARS characters ]\n'

        return file_content_string

    except Exception as e:
        f'Error reading file "{file_path}": {e}'
