# Description: This script tests various numeric
#              conversion techniques
# Author: Tihitina Z. Newprorogramer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a_float = float(a)
print(a_float)

b_int = int(b)
print(b_int)

# c_int = int(c)    # value error


# d_int = int(d)    # value error


# c_float = float(c) # value error

# d_float = float(d) # value error

a_int = int(float(a))
print(a_int)

print(a_float, type(a_float))
print(b_int, type(b_int))

c_num = c[:3]
print(c_num)

d_num = d[-2]

print(d_num)
print(a.strip())
print(d.strip())
