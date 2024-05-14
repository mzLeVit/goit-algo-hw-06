import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


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

    def __str__(self):
        return f"Контактна особа: {self.name.value}, телефони: {'; '.join(str(p) for p in self.phones)}"
    
    def add_phone(self, number):
        try:
            phone = Phone(number)
            self.phones.append(phone)
            return f"Phone number '{number}' added for {self.name.value}."
        except ValueError as e:
            return str(e)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                return f"Phone number '{number}' removed for {self.name.value}."
        return f"Phone number '{number}' not found for {self.name.value}."

    def edit_phone(self, old_number, new_number):
        try:
            new_phone = Phone(new_number)
            for phone in self.phones:
                if phone.value == old_number:
                    phone.value = new_number
                    return f"Phone number '{old_number}' edited to '{new_number}' for {self.name.value}."
            return f"Phone number '{old_number}' not found for {self.name.value}."
        except ValueError as e:
            return str(e)

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
            return "Record added successfully"
        else:
            return "Record already exists"

    def find_record(self, name):
        return self.data.get(name)  # Використовуємо метод get(), який повертає None, якщо запис не знайдено

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record for {name} removed from the address book."
        else:
            return f"No record found for {name}."

    def find(self, param):
        record = self.find_record(param)
        if record:
            return record
        else:
            return None






if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete_record("Jane")
