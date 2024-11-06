# Из цельсия в фаренгейты
import random
import math
c = input("Введите температуру в Цельсиях ")
f = float(c) * 1.6 + 32

print(str("Температура в Фаренгейтах "), float(f))



#Угадай число


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        try:
            user_guess = int(input("Введи свое число: "))
            attempts += 1

            if user_guess < number_to_guess:
                 print("Загаданное число больше. Попробуй еще раз.")
            elif user_guess > number_to_guess:
                 print("Загаданное число меньше. Попробуй еще раз.")
            else:
                 print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.")
                 break
        except ValueError:
            print("Пожалуйста, введи корректное число.")

guess_the_number()

#Вычесление Индекса Массы Тела


def BMI():
    print("Сейчас я расчитаю ваш Индекс Массы Тела")
    mass = int(input("Введите ваш вес "))
    height1 = int(input("Введите ваш рост "))
    height2 = height1 / 100 
    height3 = pow(2, height2)
    bmi = int(mass) / (height3)
    print("Ваш индекс массы тела:", int(bmi))

BMI()