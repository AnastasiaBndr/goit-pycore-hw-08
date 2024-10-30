from instances import Record, AddressBook
from command_parser import parse_input
from serialization import save_data, load_data


def main():
    filename = 'AddressBook.pkl'
    book = load_data(AddressBook(), filename)

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        name = args[0] if len(args) > 0 else None

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if name in book:
                user = book.find(name)
                user.add_phone(args[1] if len(args) > 1 else None)
                book.add_record(user)
                print("Contact updated")
                save_data(book, filename)
            else:
                record = Record(name)
                record.add_phone(args[1] if len(args) > 1 else None)
                book.add_record(record)
                save_data(book, filename)
                print("Contact added")
        elif command == "change":
            user = book.find(name)
            user.edit_phone(args[1] if len(args) > 1 else None,
                            args[2] if len(args) > 1 else None)
            book.add_record(user)
            save_data(book, filename)
            print("Contact updated")
        elif command == "phone":
            print(f"Phones for {name}: {book.show_phones(name)}")

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            user = book.find(name)
            user.add_birthday(args[1] if len(args) > 1 else None)
            book.add_record(user)
            save_data(book, filename)
            print("Contact updated")

        elif command == "show-birthday":
            print(book.show_birthday(name))

        elif command == "birthdays":
            print(book.birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
