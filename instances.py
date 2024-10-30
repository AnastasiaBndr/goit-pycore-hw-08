from collections import UserDict
from datetime import datetime, timedelta
from error_handler import input_error
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    __regex = r'^\d{10}$'

    def __init__(self, value):
        if not re.search(self.__regex, value):
            raise ValueError("Неправильний формат номера")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        self.value = datetime.strptime(value, "%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @input_error
    def add_phone(self, value: str):
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        for i in self.phones:
            if i.value == value:
                self.phones.remove(i)

    def find_phone(self, value: str):
        for i in self.phones:
            if i.value == value:
                return i.value

    @input_error
    def edit_phone(self, started_value: str, new_value: str):
        counter = 0
        for i in self.phones:
            if i.value == started_value:
                break
            counter += 1
        if counter < len(self.phones):
            self.phones[counter] = Phone(new_value)

    @input_error
    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = {'phones': list(
            map(lambda x: x.value, record.phones)),
            'birthday': record.birthday.value.strftime("%d.%m.%Y") if record.birthday != None else 'No info'}

    def find(self, name: str):
        record = Record(name)
        phones = self.data.get(name)
        for i in phones['phones']:
            record.add_phone(i)
        return record

    def show_phones(self, name):
        user = self.data[name]
        return user["phones"]

    def delete(self, value: str):
        del self.data[value]

    @input_error
    def birthdays(args, book):
        current_date = datetime.today().date()
        users_birthday = []
        for name, info in book.items():
            birthday = datetime.strptime(info["birthday"], "%d.%m.%Y").date()
            birthday_this_year = datetime(
                year=current_date.year, day=birthday.day, month=birthday.month).date()
            time_difference = birthday_this_year - current_date

            if (0 <= time_difference.days < 7) or \
                (-366 <= time_difference.days < -359) or \
                    (-365 <= time_difference.days < -358):
                if birthday_this_year.weekday() == 5:
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year += timedelta(days=1)

                users_birthday.append(
                    {"name": name, "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")})

        return users_birthday

    @input_error
    def show_birthday(self, name):
        user = self.data[name]
        return user["birthday"]
