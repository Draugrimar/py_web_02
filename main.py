phone_book = {}


def main():  # Основной модуль
    while True:
        user_input = input("Please enter your command: ")
        result = parcer(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()


def input_error(func):  # Декоратор ошибок
    def inner_func(text):
        try:
            return func(text)
        except IndexError:
            return "Please enter command, name and phone number"
        except KeyError:
            return "No such name in the phone book"
        except ValueError:
            return "Please enter correct number"

    return inner_func


def normalize(text):
    return text.lower()


@input_error  # Парсер команд
def parcer(text):
    line = text.split(" ")
    command = normalize(line[0])
    if command == "hello":
        return "Hi! How can I help you?"
    if command in ["good bye", "close", "exit"]:
        return "Good bye!"
    if command == "add":
        return add(f"{command} {line[1]} {line[2]}")
    if command == "change":
        return change(f"{command} {line[1]} {line[2]}")
    if command == "phone":
        return phone(f"phone {line[1]}")
    if command == "show" and normalize(line[1]) == "all":
        return get_phone_book()
    else:
        return "Unknown command, please try again"


@input_error
def add(text):  # Добавление новых контактов
    text = text.split(" ")
    if text[1] not in phone_book:
        phone_book.update({text[1]: text[2]})
        return "Completed!"
    else:
        return "Such name already exists"


@input_error
def change(text):  # Изменение существующих контактов
    text = text.split(" ")
    phone_book.pop(text[1])
    phone_book.update({text[1]: text[2]})
    return "Completed!"


@input_error
def phone(text):  # Достаём контак по имени
    text = text.split(" ")
    return phone_book[text[1]]


def get_phone_book():  # Вывод всей телефонной книги
    result = ""
    for name, phone in phone_book.items():
        result += "\n" + name + " " + phone
    return result


if __name__ == "__main__":
    main.run(debug=False, host="0.0.0.0")
