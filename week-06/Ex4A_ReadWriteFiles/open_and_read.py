f = open("about_me.txt", "r")
# print(f.read()) # returning everything
f.close()
f = open("about_me.txt", "r")
# print(f.read(50))  # Returning 50 characters
# print(f.read(50)) # continuing from where it has stopped 
# print(f.readline(10)) # reading the first line 10 characters
# print(f.readline()) # It returned the remaining character from first line
f.close()
f = open("about_me.txt", "r")
f.close()
# for i in range(1, 5):
# print(f.readline()) # when the rest are commented out it resturns the first 4 lines line by line
f = open("about_me.txt", "r")
# print(f.readlines(1)) # returns the first line and it is a list and untill the line break
# print(f.readlines(1)) # it returns the second line since it continued
# print(f.readlines(10)) # returned the third line untill the line break even tho the range was 10
# print(f.readlines(10)) # It started from the first line and second line
# print(f.readlines(100))  # returned a list 
# print(f.readlines(-1)) # It returned everything 

f = open("about_me.txt", "r")
variable1 = f.read(50) # the first 50 characters
variable2 = [] # the next 4 lines 
for i in range(1, 5):
    variable2.append(f.readline()) # adding the lines
variable3 = f.readlines(100) # reads the next 100 characters as lines

print("First 50 characters:", variable1) 
print("Next four lines, as list by line:", variable2)
print("Next 100 characters, as list by line, rounded up to complete lines:", variable3)