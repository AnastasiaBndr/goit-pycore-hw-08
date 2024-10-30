import pickle
from instances import AddressBook


def save_data(book, filename):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(address_book: AddressBook, filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return address_book()
