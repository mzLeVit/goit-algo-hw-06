import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, number):
        if not re.match(r'^\d{10}$', number):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        try:
            phone = Phone(number)
            self.phones.append(phone)
            print(f"Phone number '{number}' added for {self.name.value}.")
        except ValueError as e:
            print(e)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                print(f"Phone number '{number}' removed for {self.name.value}.")
                return
        print(f"Phone number '{number}' not found for {self.name.value}.")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                print(f"Phone number '{old_number}' edited to '{new_number}' for {self.name.value}.")
                return
        print(f"Phone number '{old_number}' not found for {self.name.value}.")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                print(f"Phone number '{number}' found for {self.name.value}.")
                return
        print(f"Phone number '{number}' not found for {self.name.value}.")


class AddressBook(UserDict):
    def add_record(self, name):
        self.data[name] = Record(name)

    def find_record(self, name):
        if name in self.data:
            return self.data[name]
        print(f"No record found for {name}.")

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Record for {name} removed from the address book.")
        else:
            print(f"No record found for {name}.")


# Приклад використання
address_book = AddressBook()
address_book.add_record("John Doe")
record = address_book.find_record("John Doe")
if record:
    record.add_phone("1234567890")
    record.add_phone("9876543210")
    record.remove_phone("1234567890")
    record.edit_phone("9876543210", "9999999999")
    record.find_phone("9999999999")
address_book.delete_record("John Doe")
