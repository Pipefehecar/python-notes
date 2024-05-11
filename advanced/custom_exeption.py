class CustomError(Exception):
    def __init__(self, message: str, error_code: int):
        self.message = message
        self.error_code = error_code
        super().__init__(
            f"El error es: {self.message} con code: {self.error_code}",
            self.message,
            self.error_code,
        )

    def __str__(self):
        return f"El error es: {self.message} con code: {self.error_code}"

    def custom_method(self):
        print("Custom method")

    def __reduce__(self):
        return CustomError, (self.message, self.error_code)


if __name__ == "__main__":
    try:
        raise CustomError("Error personalizado", 500)
    except CustomError as e:
        print(e)
        e.custom_method()
        print(e.message)
        print(e.error_code)
        print(e.__reduce__())
        print(e.__str__())
