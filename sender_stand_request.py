import configuration
import requests
import data


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

# Получение аутентификатора для пользователя
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")

# Создание набора
def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers={
                             "Authorization": "Bearer " + get_new_user_token()
                         })
