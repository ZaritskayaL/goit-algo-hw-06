<Address Book — OOP Python Project>
Цей проєкт реалізує адресну книгу з використанням принципів об’єктно‑орієнтованого програмування (OOP).
Система складається з класів <Field>, <Name>, <Phone>, <Record> та <AddressBook>, які разом забезпечують зберігання та управління контактами.

<Структура класів>
Field
Базовий клас для всіх полів запису.

Містить:

атрибут value

метод __str__

<Name>
Наслідує Field.
Використовується для зберігання імені контакту.

<Phone>
Наслідує Field.
Містить валідацію номера телефону:

тільки цифри

рівно 10 символів

При некоректному вводі піднімає ValueError.

<Record>
Представляє один контакт.

Містить:

name — об’єкт Name

phones — список об’єктів Phone

Методи:

add_phone(phone)

remove_phone(phone_value)

edit_phone(old, new)

find_phone(phone_value)

__str__ — форматований вивід

<AddressBook>
Наслідує UserDict.

Функціональність:

add_phone(record) — додає запис у словник

find(name) — повертає Record або None

delete(name) — видаляє запис

__str__ — виводить усі записи

Приклад використання
python
book = AddressBook()

# Створення запису John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_phone(john_record)

# Створення запису Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_phone(jane_record)

# Виведення всіх записів
print(book)

# Редагування телефону John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Пошук конкретного телефону
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")
📌 Валідація телефонів
Клас Phone гарантує, що номер:

є рядком

складається лише з цифр

має довжину 10 символів

При порушенні умов:

Kód
ValueError: Phone number must contain only digits and be 10 characters long.
🧩 Формат виводу
При друці Record:

Kód
Name: John, Phones: 1112223333, 5555555555
При друці AddressBook:

Kód
Name: John, Phones: 1112223333, 5555555555
Name: Jane, Phones: 9876543210
✔️ Особливості реалізації
Використано UserDict для зручного розширення словника.

Кожен телефон — окремий об’єкт Phone.

Всі зміни (редагування, видалення) виконуються через методи класів.

Код легко розширити (наприклад, додати email, адресу, дату народження).