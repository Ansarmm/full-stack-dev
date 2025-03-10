import os 

def print_directory_structure(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item) 
        if os.path.isdir(path):
            print_directory_structure(path)  # Рекурсивный вызов для папки
        else:
            print(path)  # Выводим путь к файлу
dir_list = print_directory_structure("/Users/ansar/workspace/skool")



def find_directory(target_dir, search_path):
    for item in os.listdir(search_path):  # Перебираем файлы и папки
        full_path = os.path.join(search_path, item)
        if os.path.isdir(full_path):  # Если это папка
            if item == target_dir:  # Проверяем, та ли это папка
                return full_path
            # Рекурсивный вызов внутри текущей папки
            result = find_directory(target_dir, full_path)
            if result:
                return result
    return None  # Если не нашли

# Пример использования:
directory_name = "dev-core"  # Имя папки, которую ищем
search_path = "/Users/ansar"  # Где ищем
found_path = find_directory(directory_name, search_path)
if found_path:
    print(f"Директория найдена: {found_path}")
else:
    print("Директория не найдена.")



def calculate_total_size(directory):
    total_size = 0  # Начинаем с нуля
    for item in os.listdir(directory):  
        path = os.path.join(directory, item)  # Полный путь к файлу/папке
        
        if os.path.isfile(path):  # Если это файл, считаем его размер
            total_size += os.path.getsize(path)
        
        elif os.path.isdir(path):  # Если это папка, вызываем рекурсию
            total_size += calculate_total_size(path)
    
    return total_size  # Возвращаем общий размер

directory = "/Users/ansar/workspace"  # Папка, которую будем проверять
total_size = calculate_total_size(directory)  # Запускаем функцию
print(f"Общий размер файлов в '{directory}': {total_size} байт")