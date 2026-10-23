import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_path = os.path.abspath(working_directory)
    fullpath = os.path.normpath(os.path.join(abs_path, file_path))
    valid_target = os.path.commonpath([abs_path, fullpath]) == abs_path
    if not valid_target:
        return f"Error: Cannot read {file_path} as it is outside the permitted working directory"
    if os.path.isdir(fullpath):
        return f"Error: Cannot write to \"{file_path}\" as it is a directory" 
    os.makedirs(os.path.dirname(fullpath), exist_ok=True)
    with open(fullpath, "w") as f:
        f.write(content)
    return f"Successfully wrote to \"{file_path}\" ({len(content} characters written)"

