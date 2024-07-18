### Тесты на проверку параметра Name при создании набора для конкретного пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
### Чеклист для автотестов:
|№	           Описание	                                                  ОР
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| 
|1	Допустимое количество символов (1):                      |            Код ответа — 201                               |
|   kit_body = {                                             |    В ответе поле name совпадает с полем name в запросе    |
|   "name": "a"                                              |                                                           |
|   }	                                                       |                                                           |
|2	Допустимое количество символов (511):                    |                                                           |
|   kit_body = {                                             |    Код ответа — 201                                       | 
|   "name":"Тестовое значение для этой проверки будет ниже"  |    В ответе поле name совпадает с полем name в запросе    |
|    }	                                                     |                                                           |
|3	Количество символов меньше допустимого (0):              |                                                           |
|    kit_body = {                                            |    Код ответа — 400                                       |
|    "name": ""                                              |                                                           |
|    }	                                                     |                                                           |
|4	Количество символов больше допустимого (512):            |                                                           |
|    kit_body = {                                            |    Код ответа — 400                                       |
|    "name":"Тестовое значение для этой проверки будет ниже" |                                                           |  
|    }	                                                     |                                                           |
|5	Разрешены английские буквы:                              |                                                           |
|    kit_body = {                                            |    Код ответа — 201                                       |
|    "name": "QWErty"                                        |    В ответе поле name совпадает с полем name в запросе    |
|    }	                                                     |                                                           |
|6	Разрешены русские буквы:                                 |                                                           | 
|    kit_body = {                                            |    Код ответа — 201                                       |
|    "name": "Мария"                                         |    В ответе поле name совпадает с полем name в запросе    |
|    }	                                                     |                                                           |
|7	Разрешены спецсимволы:                                   |                                                           |
|    kit_body = {                                            |    Код ответа — 201                                       |
|    "name": ""№%@","                                        |    В ответе поле name совпадает с полем name в запросе    |
|    }	                                                     |                                                           |
|8	Разрешены пробелы:                                       |                                                           |
|    kit_body = {                                            |    Код ответа — 201                                       | 
|    "name": " Человек и КО "                                |    В ответе поле name совпадает с полем name в запросе    |
|     }	                                                     |                                                           |
|9	Разрешены цифры:                                         |                                                           |
|    kit_body = {                                            |    Код ответа — 201                                       |
|    "name": "123"                                           |    В ответе поле name совпадает с полем name в запросе    |
|    }	                                                     |                                                           |
|10	Параметр не передан в запросе:                           |                                                           |
|    kit_body = {                                            |     Код ответа — 400                                      |
|    }	                                                     |                                                           |
|11	Передан другой тип параметра (число):                    |                                                           |
|    kit_body = {                                            |     Код ответа — 400                                      |
|    "name": 123                                             |                                                           |
|    }	                                                     |                                                           |


#### Тестовые значения для проверок №2 и №4

Допустимое количество символов (511):
kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

Количество символов больше допустимого (512):
kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
### Шаги выполнения проекта

1. Написать `POST`-запрос на создание нового пользователя и запомнить токен авторизации authToken.
2. Написать `POST`-запрос на создание личного набора для этого пользователя. Обязательно передать заголовок Authorization.
3. Написать функции для проверки позитивных и негативных сценариев по готовому чек-листу.
4. Запустить автотест с помощью Pytest.
5. Заархивировать папку с проектом `configuration.py`, `data.py`, `sender_stand_request.py`, `create_kit_name_kit_test.py`, `README.md`, `.gitignore` в ZIP-архив.
