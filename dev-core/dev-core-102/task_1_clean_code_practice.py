import time

start_time = time.time()
price = float(input("Enter your price: "))
name = input("Enter your name: ")

loyalty_list = ["Ansar", "Bolat", "Alibek"]
added_name = input("Enter name that will added into loyalty list: ")
loyalty_list.append(added_name)


def apply_basic_discount(price, basic_discount_rate):
    return price - price * basic_discount_rate


def apply_loyalty_discount(price, loyalty_discount_rate):
    if name in loyalty_list:
        return price * loyalty_discount_rate


end_time = time.time()
execution_time_minutes = int((end_time - start_time) / 60)


def apply_basic_tax(price, tax_rate):
    return price * tax_rate


def apply_wildcard_tax(price, wildcard_tax_rate):
    if execution_time_minutes % 2 == 1:
        return price * wildcard_tax_rate


basic_discount_price = apply_basic_discount(price, 0.1)
loyalty_discount_decrease = apply_loyalty_discount(price, 0.5)
basic_tax_additive = apply_basic_tax(price, 0.15)
wildcard_tax_additive = apply_wildcard_tax(price, 0.2)


def calc_total_price():
    if (
        execution_time_minutes % 2 == 1 and name in loyalty_list
    ):  # If the program execution time is odd tax added and if name is in loyalty list decrease added
        return (
            basic_discount_price
            - loyalty_discount_decrease
            + basic_tax_additive
            + wildcard_tax_additive
        )
    elif name in loyalty_list:  # if name in loyalty list decrease added
        return basic_discount_price - loyalty_discount_decrease + basic_tax_additive
    elif (
        execution_time_minutes % 2 == 1
    ):  # if the program execution time is odd tax added
        return basic_discount_price + basic_tax_additive + wildcard_tax_additive
    else:  # basic tax and basic discount are ALWAYS added
        return basic_discount_price + basic_tax_additive


total_price = calc_total_price()


print("This is your total price: ", total_price)
