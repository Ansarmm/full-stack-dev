import time

def client_request():
    print("Клиент отправляет запрос на сервер")
    time.sleep(1)
    server_response()

def server_response():
    print("Сервер обрабатывает запрос")
    time.sleep(1)
    print("Сервер отправляет ответ: Добро пожаловать в интернет!")

client_request()