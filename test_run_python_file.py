from functions.run_python_file import run_python_file

def test_run_python_file():
    print("Result for calculator/main.py using no arguments:")
    print(run_python_file("calculator", "main.py"))

    print("Result for calculator/main using ['3 + 5'] arguments:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Result for calculator/tests.py:")
    print(run_python_file("calculator", "tests.py"))

    print("Result for ../main.py:")
    print(run_python_file("calculator", "../main.py"))

    print("Result for nonexistent.py:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("Result for lorem.txt:")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    test_run_python_file()
