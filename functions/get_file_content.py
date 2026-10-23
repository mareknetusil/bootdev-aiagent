import os

from config import MAX_READ_SIZE


def get_file_content(working_directory: str, file_path: str) -> str:
    abs_path = os.path.abspath(working_directory)
    fullpath = os.path.normpath(os.path.join(abs_path, file_path))
    valid_target = os.path.commonpath([abs_path, fullpath]) == abs_path
    if not valid_target:
        return f"Error: Cannot read {file_path} as it is outside the permitted working directory"
    if not os.path.isfile(fullpath):
        return f"Error: File not found or is not a regular file: {file_path}"

    with open(fullpath, "r") as f:
        try:
            content = f.read(MAX_READ_SIZE)
            if f.read(1):
                content += f"[...File \"{file_path}\" truncated at {MAX_READ_SIZE} characters]"
        except Exception as e:
            return f"Error: {e}"

    return content

