from functions.run_python_file import run_python_file

def test_case(file_path: str, args: list[str]) -> None:
    print(f"file_path: {file_path}, args: {args}")
    print("------------------------------------------------")
    print(run_python_file("calculator", file_path, args))

test_fixtures = [
    ("main.py", None),
    ("main.py", ["3 + 5"]),
    ("tests.py", None),
    ("../main.py", None),
    ("nonexistent.py", None),
    ("lorem.txt", None)
]

for file_path, args in test_fixtures:
    test_case(file_path, args)
