from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, phone):
        if type(phone) != str:
            raise TypeError("Phone number must be a string.")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must contain only digits and be 10 characters long.")
        
        self._value = phone

class Record:
    
    def __init__(self, name):
        if isinstance(name, Name):
            self.name = name
        else:
            self.name = Name(name)
        
        self.phones: list[Phone] = []
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone_value: str):
        for p in self.phones:
            if p.value == phone_value:
                return p
        return None
    
    def remove_phone(self, phone_value: str):
        for p in self.phones:
            if p.value == phone_value:
                self.phones.remove(p)
                return True
        raise ValueError("Phone number not found.")
    
    def edit_phone(self, old_phone: str, new_phone: str):
        phone_obj = self.find_phone(old_phone)
        if not phone_obj:
            raise ValueError("Old phone number not found.")
        
        Phone(new_phone) 
        
        phone_obj.value = new_phone
        return True
    
    
    
    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"
    
class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
            return True
        return False
    
    def find(self, name):
        return self.data.get(name)
    
    def __str__(self):
        if not self.data:
            return "Address Book is empty."
        
        return '\n'.join(str(record) for record in self.data.values())
    

book = AddressBook()

    
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    
book.add_record(john_record)

   
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)
  
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")
