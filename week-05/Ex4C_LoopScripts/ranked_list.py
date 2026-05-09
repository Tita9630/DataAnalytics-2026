favorite_foods = ["injera", "spageti", "pizza", "burger", "lasagna"]
for index, food in enumerate(reversed(favorite_foods), start=1):
    if index == 1:
        print(index, food, "<- top pick!")
    else:
        print(index, food)