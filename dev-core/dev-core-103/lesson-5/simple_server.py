import socket

# Ввод порта от пользователя
port = 8000

# Создание TCP-сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', port))
server_socket.listen(1)

print(f"Сервер запущен на порту {port}.")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")

    # Отправка сообщения клиенту
    client_socket.sendall(b"Hello, World!\n")

    # Закрытие соединения
    client_socket.close()