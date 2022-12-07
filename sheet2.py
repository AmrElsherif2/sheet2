# sheet 2 p 1
import math as m

a = float(input("angle in degree ="))
z = m.sin(a * m.pi / 180)
print("angle in degree=" + str(a), "where its sin=" + str(z))

# ---------------------------------------------------------

# sheet 2 p 2
num = int(input("num : "))
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# ----------------------------------------------------------------

# sheet 2 p 3
import math

x = float(input("input num :"))
if x >= 4:
    y = math.sqrt(x)
    print(y)
elif x < 0:
    y = x ** 2
    print(y)
else:
    y = (x + 2) / 2
    print(y)

# -------------------------------------------------------------------

# sheet 2 p 4
# a
print(bool(3 * 4 == 2 * 6 or (8 - 2) / 2 == 3 and not 2 ** 3 == 8))
# b
print(bool(3 * 4 == 2 * 6 or (8 - 2) / 2 == 3))
# c
print(bool(not 3 == 3 and 7 > 6))
# d
c = 10
if c:
    d = c
    print(d)
# e

s = 0
if s:
    q = s
    print(q)

# -----------------------------------------------------------

# sheet 2 p 5
