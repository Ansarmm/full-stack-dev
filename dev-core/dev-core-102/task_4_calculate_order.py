from datetime import datetime

loyalty_list = ["Ansar", "Bolat", "Alibek"]

price = int(input("Enter your order amount: "))
name = input("Enter your name: ")


def apply_amount_discount(price, amount_discount_rate):
    if price > 1000:
        return price * amount_discount_rate
    else:
        return 0


def apply_loyalty_discount(price, loyalty_discount_rate):
    if name in loyalty_list:
        return price * loyalty_discount_rate
    else:
        return 0


current_minute = datetime.now().minute


def apply_tax(price, wildcard_tax_rate): #If current minute is odd, no tax is applied
    if current_minute % 2 == 1:
        return price * wildcard_tax_rate
    else:
        return 0


promo = input("Do you know any promocodes?: ")


def apply_promo_discount(price, promo):
    if promo == "DISCOUNT2024":
        return price * 0.05
    else:
        return 0


amount_discount = apply_amount_discount(price, 0.05)
loyalty_discount = apply_loyalty_discount(price, 0.1)
promo_discount = apply_promo_discount(price, promo)
tax = apply_tax(price, 0.05)

total_price = price - amount_discount - loyalty_discount - promo_discount + tax
print("Total price: ", total_price)
