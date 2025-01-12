num_items = int(input("Enter numbers of orders: ")) #Enter quantity of orders
prices = []
for i in range(1, num_items + 1): #Enter prices of each order
    price = float(input(f"Enter price of order N{i}: "))
    prices.append(price) #add prices of orders into list
expensive = list(filter(lambda x: x > 1000, prices)) #prices over 1000
unexpensive = list(filter(lambda x: x < 1000, prices)) #prices under 1000
discounted = list(map(lambda x: x * 0.9, expensive)) #apply discount on orders over 1000
total = sum(discounted) + sum(unexpensive) #Sum of orders under 1000 and over 1000 with discount
print(total)