from functions.get_file_content import get_file_content

def test_get_file_content():
    print("Result for lorem.txt:\n")
    print(get_file_content("calculator", "lorem.txt"))
    print("Result for main.py:\n")
    print(get_file_content("calculator", "main.py"))
    print("Result for pkg/calculator.py:\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Result for /bin/cat:\n")
    print(get_file_content("calculator", "/bin/cat"))
    print("Result for pkg/does_not_exist.py:\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test_get_file_content()

