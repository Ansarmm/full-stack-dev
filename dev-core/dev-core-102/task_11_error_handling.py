while True:
    try:
        quantity = int(input("Введите количество продуктов: "))
        if quantity < 0:
            print("Ошибка, введите положительное целое число") 
        elif quantity > 1000:
            print("Ошибка, введите число меньше 1000")
        else:
            break
    except ValueError:
        print("Ошибка, введите целое число")      
while True:
    try: 
        price = float(input("Введите цену за 1 продукт: "))
        if price < 0:
            print("Введите положительное число")
        elif price > 1000:
            print("Ошибка, введите число меньше 1000")
        else:
            break
    except ValueError:
        print("Ошибка, введите число")
total_price = price * quantity
print(f"Итоговая цена {quantity} продуктов по {price} стоимости равна: {total_price}")