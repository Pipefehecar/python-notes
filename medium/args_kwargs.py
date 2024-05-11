def do_something(*args, **kwargs):
    print(f"args: {args}, type args: {type(args)}")
    print(f"kwargs: {kwargs}, type kwargs: {type(kwargs)}")


if __name__ == "__main__":
    do_something(1,'dos',3, color='azul', marca='adidas')