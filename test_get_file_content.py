from functions.get_file_content import get_file_content


def test_case(file_path: str) -> None:
    result = get_file_content("calculator", file_path)
    print(f"{file_path} length: {len(result)}")
    print(f"{file_path} truncated: {'truncated' in result}")
    print(result)

test_fixtures = [
    "lorem.txt",
    "main.py",
    "pkg/calculator.py",
    "/bin/cat",
    "pkg/does_not_exist.py"
]

for fixture in test_fixtures:
    test_case(fixture)
