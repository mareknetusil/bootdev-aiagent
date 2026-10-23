from functions.write_file import write_file


def test_case(file_path: str, content: str) -> None:
    response = write_file("calculator", file_path, content)
    print(response)


test_fixtures = [
    ("lorem.txt", "wait, this isn't lorem ipsum"),
    ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("/tmp/temp.txt", "this should not be allowed"),
]

for file_path, content in test_fixtures:
    test_case(file_path, content)
