recipe_prices = {
    "Borsch": 3000,
    "Pilaf": 2500,
    "Salad": 1500,
    "Steak": 5000
}

for recipes, prices in recipe_prices.items():
    print(f"Цена {recipes}: {prices} тенге")

def bubble_sort(recipe_prices):
    recipes = list(recipe_prices.items())  
    n = len(recipe_prices)
    for i in range(n):
        for j in range(0, n - i - 1):
            if recipes[j][1] > recipes[j + 1][1]:
                recipes[j], recipes[j + 1] = recipes[j + 1], recipes[j]
    return dict(recipes)

sorted_recipes = bubble_sort(recipe_prices)

selected_recipes = []
quantity_of_recipes = int(input("Введите количество рецептов которые хотите приготовить: "))
for i in range(quantity_of_recipes):
    selected_recipe = input("Введите выбранный рецепт: ").strip()
    selected_recipes.append(selected_recipe)

prices_list = []
for recipes, prices in sorted_recipes.items():
    prices_list.append(recipes)
print("Отсортированный список рецептов по ценам: ")
print(prices_list)

budget = int(input("Введите ваш бюджет: "))
accesible_recipes_list = []
def accesible_recipes(budget):
    for recipe in selected_recipes:
        budget -= recipe_prices[recipe]
        if budget > 0:
            accesible_recipes_list.append(recipe)
accesible_recipes(budget)
print("Вы можете позволить себе эти рецепты учитывая ваш бюджет: ", accesible_recipes_list)