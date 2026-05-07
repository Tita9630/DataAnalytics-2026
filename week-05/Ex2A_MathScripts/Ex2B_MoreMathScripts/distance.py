import math
x1 = 200
x2 = 320
y1 = 440
y2 = 560

x_difference = x2 - x1
y_difference = y2 - y1
distance = math.sqrt(x_difference ** 2 + y_difference ** 2)
print(f"The distance is {distance:.2f}")