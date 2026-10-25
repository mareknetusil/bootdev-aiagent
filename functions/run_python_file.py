import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    abs_path = os.path.abspath(working_directory)
    fullpath = os.path.normpath(os.path.join(abs_path, file_path))
    valid_target = os.path.commonpath([abs_path, fullpath]) == abs_path
    print(f"{abs_path=}\t {fullpath=}\t {valid_target=}")
    if not valid_target:
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    if not os.path.isfile(fullpath):
        return f"Error: \"{file_path}\" does not exist or is not a regular file"
    if not file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file"

    command = ["python", fullpath]
    if args:
        command.extend(args)
    PIPE = subprocess.PIPE
    retval = subprocess.run(command, text=True, timeout=30, stdout=PIPE, stderr=PIPE)
    response = ""
    if retval.returncode != 0:
        response += "Process exited with code X "
    if retval.stdout == "" and retval.stderr == "":
        response += "No output produced "
    response += f"STDOUT: {retval.stdout}"
    response += f"STDERR: {retval.stderr}"

    return response

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file as a program in the working directory tree. It returns the output of the execution to stdout/stderr",
        "parameters": {
            "type": "object",
            "required": ["file_path", "args"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the python script, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": "string",
                    "description": "Positional arguments to be passed to the python script.",
                },
            },
        },
    },
}
