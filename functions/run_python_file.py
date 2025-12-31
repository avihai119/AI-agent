import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_pwd_path = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(abs_pwd_path, file_path))
        valid_target_file = os.path.commonpath([abs_pwd_path, path_to_target_file]) == abs_pwd_path

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path_to_target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", path_to_target_file]

        if args is not None:
            command.extend(args)

        run_python_process = subprocess.run(command, cwd=abs_pwd_path, 
                                            capture_output=True, text=True, timeout=30)
        output_list = []

        if run_python_process.returncode != 0:
            output_list.append(f"Process exited with code {run_python_process.returncode}")
        if not run_python_process.stdout and not run_python_process.stderr:
            output_list.append("No output produced")
        if run_python_process.stdout:
            output_list.append(f"STDOUT:\n {run_python_process.stdout}")
        if run_python_process.stderr:
            output_list.append(f"STDERR:\n {run_python_process.stderr}")

        return "\n".join(output_list)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
