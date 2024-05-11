def example_generator():
    for i in range(1, 11):
        yield i


if __name__ == "__main__":
    yield_generator = (i for i in range(1, 11))
    print(f"{yield_generator=}")
    for i in yield_generator:
        print(i)
    try:
        print(f"{next(yield_generator)=}")
    except StopIteration as e:
        print(f"this generator is exhausted: {e}\n")

    example_gen = example_generator() # same as yield_generator
    print(f"{example_gen=}")
    for i in example_gen:
        print(i)