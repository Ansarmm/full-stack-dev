recipes = {'Pasta': ['Tomatoes', 'Cheese', 'Spaghetti']}

print("Введите 1/2/3 для разных операций")
print("1. Сохранить рецепты в файл")
print("2. Загрузить рецепты из файла")
print("3. Показать загруженные рецепты в файле")
choice = input("Введите операцию: ")

try: 
    if choice == "1":
        for recipe, ingredients in recipes.items():
            with open('recipes.txt', 'w') as file:
                file.write(f"{recipes}")
        print("Рецепты успешно сохранены!")
    if choice == "2":
        with open("recipes.txt", "r") as file:
            content = file.read()
            recipes = content
            print("Рецепты успешно загружены")
    if choice == "3":
        with open("recipes.txt", "r") as file:
            content = file.read()
        print(content)
except FileNotFoundError:
    print("Ошибка, файла не найден")