import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sum(vals_sample)) #adding 75 random values 
print("Average of 75 sample values:", statistics.mean(vals_sample)) # random average
print("Median of 75 sample values:", statistics.median(vals_sample)) # the random middle value

print("\n_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", statistics.mean(vals_choices)) #calculating average
print("Median of 200 values:", statistics.median(vals_choices)) # finding the middle value
print("Mode of 200 values:", statistics.mode(vals_choices)) # finding most common value
print("Standard deviation of 200 values:", statistics.stdev(vals_choices)) # calculating standard deviation
print("Variance of 200 values:", statistics.variance(vals_choices)) # calculating variance

area = math.pi * radius ** 2
print("\n_Modeling a random circle:")
print("Radius=", radius, ", area =", math.ceil(area), "(rounded up)") # math.celi to round up
print("Radius =", radius, ", area =", math.floor(area), "(rounded down)") # math.floor to round down