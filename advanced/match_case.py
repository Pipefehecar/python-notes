import random


def match_status(status: int) -> None:
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case 503:
            print("Service Unavailable")
        case _:
            print("Unknown status code")


def p_command(command: str) -> None:
    command: list[str] = command.split()
    match command:
        case ["start", *args]:
            print(f"Starting with args: {args if args else 'empty args'}")
        case ["stop", *args]:
            print(f"Stopping with args: {args if args else 'empty args'}")
        case ["pause", *args] if len(args) > 0:
            print(f"Pausing with args: {args if args else 'empty args'}")
        case ["exit" | "quit" | "q" | "e"]:
            print("Exiting")
        case _:
            print("Unknown command")


if __name__ == "__main__":
    status: int = random.choice([200, 404, 500, 503])
    match_status(status)
    p_command("start -d -v -f")
    p_command("stop -f")
    p_command("pause")
