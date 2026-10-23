import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.join(abs_path, directory)
    target_dir = os.path.normpath(target_dir)
    valid_target = os.path.commonpath([abs_path, target_dir]) == abs_path
    lines = [f"Result for '{directory}':"]
    if not valid_target:
        lines.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(target_dir):
        lines.append(f'Error: "{directory}" is not a directory')
    else:
        for name in os.listdir(target_dir):
            size = os.path.getsize(f"{target_dir}/{name}")
            is_dir = os.path.isdir(f"{target_dir}/{name}")
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

    return "\n\t".join(lines)

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
