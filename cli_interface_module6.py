import re


class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, number):
        if not re.match(r'^\d{10}$', number):
            raise ValueError("Phone number must be 10 digits.")
        self.number = number


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        try:
            phone = Phone(number)
            self.phones.append(phone)
            print(f"Phone number '{number}' added for {self.name.name}.")
        except ValueError as e:
            print(e)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                self.phones.remove(phone)
                print(f"Phone number '{number}' removed for {self.name.name}.")
                return
        print(f"Phone number '{number}' not found for {self.name.name}.")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.number == old_number:
                phone.number = new_number
                print(f"Phone number '{old_number}' edited to '{new_number}' for {self.name.name}.")
                return
        print(f"Phone number '{old_number}' not found for {self.name.name}.")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                print(f"Phone number '{number}' found for {self.name.name}.")
                return
        print(f"Phone number '{number}' not found for {self.name.name}.")


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, name):
        record = Record(name)
        self.records.append(record)
        print(f"Record for {name} added to the address book.")

    def find_record(self, name):
        for record in self.records:
            if record.name.name == name:
                print(f"Record found for {name}.")
                return record
        print(f"No record found for {name}.")

    def delete_record(self, name):
        record = self.find_record(name)
        if record:
            self.records.remove(record)
            print(f"Record for {name} removed from the address book.")




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
