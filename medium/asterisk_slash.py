def only_args(pos1, pos2, /):
    print(pos1, pos2)


def only_kwargs(*, kwarg1, kwarg2):
    print(kwarg1, kwarg2)


def args_kwargs(pos1, pos2, /, standard, *, kwarg1, kwarg2):
    print(kwarg1, kwarg2)
    print(pos1, pos2)
    print(standard)


if __name__ == "__main__":
    # TypeError: args_kwargs() got some positional-only arguments passed as keyword arguments: 'pos1, pos2'
    args_kwargs(1, 2, standard="stdr", kwarg1="uno", kwarg2="dos")
    # TypeError: args_kwargs() missing 2 required positional arguments: 'pos1' and 'pos2'
    # args_kwargs(1, 2, standard="stdr", kwarg1=1)

    args_kwargs(1, 2, "stdr", kwarg2=2, kwarg1=1)
