# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# функция, которая будет менять содержимое тела запроса.
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

 # Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


# Функция негативной проверки, когда в ответе ошибка про символы
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

 # Функция для негативной проверки, когда в ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

# Позитивные проверки

# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 5. Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")
# Тест 6. Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7.Разрешены спецсимволы
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8.Разрешены пробелы
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")
# Тест 9.Разрешены цифры
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Негативные проверки

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_empty_name_get_error_response():
    negative_assert("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_symbols_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_no_name(current_kit_body)

# Тест 11. Передан другой тип параметра (число)
def test_create_kit_numeric_type_name_get_error_response():
    negative_assert(123)