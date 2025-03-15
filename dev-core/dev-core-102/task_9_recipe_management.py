recipes = {
    "Pasta": ["Tomatoes", "Cheese", "Spaghetti"],
    "Salad": ["Cucumbers", "Tomatoes", "Lettuce"]
}
ingredient_prices = {
    "Tomatoes": 500,
    "Cheese": 2000,
    "Spaghetti": 1500,
    "Cucumbers": 300,
    "Lettuce": 700
}

print(f"Доступные рецепты: ", f"Паста: {recipes["Pasta"]}", f"Салат: {recipes["Salad"]}")
for ingredient, price in ingredient_prices.items():
    print(f"{ingredient}: {price} тенге")

def add_recipe():
            print("Введите новое блюдо, его ингредиенты: ")
            new_recipe = input("Введите название блюда: ")
            new_recipe_ingredients = []
            count = int(input("Введите количество ингредентов: "))
            for ingredient in range(count):
                ingredient = (input("Введите значения(На английском с большой буквы): "))# Вводим значения и превращаем в список
                new_recipe_ingredients.append(ingredient)
                ingredient_prices.setdefault(ingredient, int(input(f"Введите стоимость {ingredient} в тенге: ")))  
            recipes[new_recipe] = new_recipe_ingredients
            print("Новый рецепт успешно введен!")
            print("\nОбновленный список рецептов:")
            for recipe, ingredients in recipes.items():
                print(f"{recipe}: {ingredients}")
            for ingredient, price in ingredient_prices.items():
                print(f"{ingredient}: {price} тенге")

def calculate_price():
    selected_recipe = input("Введите выбранный рецепт: ").strip()
    if selected_recipe in recipes:
        final_price = 0
        selected_recipe_ingredients = recipes[selected_recipe]
        for ingredient in selected_recipe_ingredients:
            if ingredient in ingredient_prices:
                final_price += ingredient_prices[ingredient]
                if final_price > 3000:
                     final_price = final_price * 0.9
        print(f"Стоимость {selected_recipe}: {final_price} тенге")
    else:
        print("Введите существующий рецепт")

print("Введите 1 для добавления нового рецепта. 2 для рассчета стоимости")
while True:
    choice = input("Введите операцию: ")
    if choice == "1":
        add_recipe()
    if choice == "2":
        calculate_price()
    else:
        print("Ошибка, введите 1 или 2")
    next_operation = input("Вы хотите провести еще операции? (Введите на английском): ")
    if next_operation.lower() != "yes":
        print("Спасибо за использование") 
        break