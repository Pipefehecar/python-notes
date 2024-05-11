if __name__ == "__main__":
    _ = 5000
    a = _ + 5000
    b = 10000
    print(f"{b == a=}")
    print(f"{b is a=}")
    print(f"{b=}")
    print(f"{a=}")
    print(f"{id(b)=} {id(a)=}")


"""
== is used to compare the values of the objects
while is is used to compare the memory addresses of the objects
"""