import requests
import json

# Ссылка на сайт с постами
url = 'https://jsonplaceholder.typicode.com/posts'


# GET запрос
def GET_request():
    response = requests.get(url) 

    # Если сайт сайт доступен и возвращает положительный запрос
    if response.status_code == 200:
        # Данные (посты) в виде переменной
        data = response.json()

        # Запись данных в файл в формате json
        with open('posts_data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        
        # Вывод для пользователя
        print("Получено записей:", len(data))
        print("Записи:")
        print(data)
    #Если статус запроса не 200. Вывод сообщающий об ошибке и статус запроса
    else:
        print("Ошибка при запросе:", response.status_code)


# GET запрос по id 
def GET_by_id_request():
    response = requests.get(url)

    if response.status_code == 200:
        # Ввод id поста который желает пользователь
        id = int(input('Введите id поста: '))

        # Все посты в виде переменной
        data = response.json()

        # Пост по id в виде переменной
        data_by_id = data[id-1]

        with open('posts_data.json', 'w', encoding='utf-8') as file:
            json.dump(data_by_id, file, ensure_ascii=False, indent=2)

        print("Получено записей:", len(data))
        print("Записи:")
        print(data_by_id)
    else:
        print("Ошибка при запросе:", response.status_code)


# POST запрос
def POST_request():
    # Ввод заголовка и текста поста
    title = input('Введите заголовок поста: ')
    body = input('Введите текст поста: ')

    # Формат отправляемых данных
    payload = {
        'title': title,
        'body': body,
        'userId': 1
    }

    response = requests.post(url, json=payload)


    if response.status_code == 201:
        print("Пост успешно создан:")
        print(response.json())
    else:
        print("Ошибка:", response.status_code)

# Програма в виде функции
def http_requests():
    # Перечень операций
    print('1. GET')
    print('2. GET by id')
    print('3. POST')

    # Выбор желаемой операции 
    choice = int(input('Какую операцию вы хотите провести: '))

    # GET запрос всех данных при вводе 1
    if choice == 1:
        GET_request()

    # GET запрос поста по выбору при вводе 2
    elif choice == 2:
        GET_by_id_request()

    # POST запрос при вводе 3
    elif choice == 3:
        POST_request()

    # Сообщение о не корректном числе
    else: 
        print('Введите корректное число')

# Вызов функции
http_requests()