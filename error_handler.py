def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"{e}")
        except KeyError as e:
            print("No key available")
        except IndexError as e:
            print("Index out of range")
        except Exception as e:  # Додайте обробку несподіваних помилок
            return f"Несподівана помилка: {e}"

    return inner
