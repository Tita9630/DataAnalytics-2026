import random
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

print(random.choice(products)) #choose 1 random product

print(random.sample(products, 3)) # choose multiple(3) items

random.shuffle(products) #rearranging the products
print(products)

print("Daily transactions:", random.randint(50, 300)) # random integer of daily transaction

