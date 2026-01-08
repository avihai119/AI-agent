import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write/overwrite to the target file in a specified file path relative to the working directory, providing error or success messages of the write output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write/overwrite to the target file, relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write/overwrite to the target file"
            )
        },
        required=["file_path", "content"]
    ),
)

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
