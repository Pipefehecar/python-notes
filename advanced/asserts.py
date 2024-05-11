def start_program(data: dict):
    """ Start the program
    """
    assert data["user"] == "admin", "Only admin can start the program"
    assert data["password"] == "admin", "Wrong password"
    assert isinstance(data, dict), "Data must be a dictionary"

    print("Program started")
    assert 1 == 1
    print("Program finished")


if __name__ == "__main__":
    print(f"{__debug__=}")
    data = {"user": "admin", "password": "admin"}
    start_program(data)
    data = {"user": "user", "password": "user"}
    start_program(data)

"""
For run without asserts:
python -O advanced/asserts.py
For run without asserts and comments:
python -OO advanced/asserts.py
"""