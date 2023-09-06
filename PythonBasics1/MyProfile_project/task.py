# MyProfile app
separator = "------------------------------------------"

# user profile
name = ""
age = 0
phone = ""
email = ""
postal_code = ""
postal_address = ""
info = ""
# business info
ogrnip = ""
inn = ""
settlement_account_num = ""
bank_name = ""
bik = ""
correspondent_account = ""


def extract_digits(number, prefix=""):
    extracted_number = ""
    for symbol in number:
        if symbol == prefix or ("0" <= symbol <= "9"):
            extracted_number += symbol
    return extracted_number


def get_and_validate(text, length):
    error_message = f"{text.capitalize()} должен содержать {length} цифр"
    while True:
        user_text = input(f"Введите {text}: ")
        only_digits = extract_digits(user_text)
        if len(user_text) == length and user_text == only_digits:
            return user_text
        else:
            print(error_message)


def general_info_user(
    name_parameter,
    age_parameter,
    phone_parameter,
    email_parameter,
    postal_code_parameter,
    postal_address_parameter,
    info_parameter,
):
    print(separator)
    print("{:<8}".format("Имя:"), name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = "лет"
    elif age_parameter % 10 == 1:
        years_parameter = "год"
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = "года"
    else:
        years_parameter = "лет"

    print("{:<8}".format("Возраст:"), age_parameter, years_parameter)
    print("{:<8}".format("Телефон:"), phone_parameter)
    print("{:<8}".format("Индекс:"), postal_code_parameter)
    print("{:<8}".format("Адрес:"), postal_address_parameter)
    print("{:<8}".format("E-mail:"), email_parameter)
    if info_parameter:
        print("")
        print("Дополнительная информация:")
        print(info_parameter)


print("Приложение MyProfile")
print("Сохраняй информацию о себе и выводи ее в разных форматах")

while True:
    # main menu
    print(separator)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию")
    print("2 - Вывести информацию")
    print("0 - Завершить работу")

    option = int(input("Введите номер пункта меню: "))
    if option == 0:
        break

    elif option == 1:
        # submenu 1: edit info
        while True:
            print(separator)
            print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Информация о предпринимателе")
            print("0 - Назад")

            option2 = int(input("Введите номер пункта меню: "))
            if option2 == 0:
                break
            elif option2 == 1:
                # input general info
                name = input("Введите имя: ")
                while 1:
                    # validate user age
                    age = int(input("Введите возраст: "))
                    if age > 0:
                        break
                    print("Возраст должен быть положительным")

                phone_input = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
                phone = extract_digits(phone_input, prefix="+")
                email = input("Введите адрес электронной почты: ")
                postal_code_input = input("Введите почтовый индекс: ")
                postal_code = extract_digits(postal_code_input)
                postal_address = input("Введите почтовый адрес (без индекса): ")
                info = input("Введите дополнительную информацию:\n")

            elif option2 == 2:
                ogrnip = get_and_validate("ОГРНИП", 15)
                inn = input("Введите ИНН: ")
                settlement_account_num = get_and_validate("расчетный счет", 20)
                bank_name = input("Введите название банка: ")
                bik = input("Введите БИК: ")
                correspondent_account = input("Введите корреспондентский счет: ")

            else:
                print("Введите корректный пункт меню")
    elif option == 2:
        # submenu 2: print info
        while True:
            print(separator)
            print("ВЫВЕСТИ ИНФОРМАЦИЮ")
            print("1 - Общая информация")
            print("2 - Вся информация")
            print("0 - Назад")

            option2 = int(input("Введите номер пункта меню: "))
            if option2 == 0:
                break
            elif option2 == 1 or option2 == 2:
                general_info_user(
                    name, age, phone, email, postal_code, postal_address, info
                )
                if option2 == 2:
                    # print business info
                    print("")
                    print("Информация о предпринимателе")
                    print("{:<8}".format("ОГРНИП:"), ogrnip)
                    print("{:<8}".format("ИНН:"), inn)
                    print("Банковские реквизиты")
                    print("{:<8}".format("Р/с:"), settlement_account_num)
                    print("{:<8}".format("Банк:"), bank_name)
                    print("{:<8}".format("БИК"), bik)
                    print("{:<8}".format("К/с"), correspondent_account)
            else:
                print("Введите корректный пункт меню")
    else:
        print("Введите корректный пункт меню")
