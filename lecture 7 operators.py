

a = 1 + 2
b = 4
c = b - a - 1
d = a * b
# e = d / c       # ZeroDivisionError
f = 3**2
g = 4**(1 / 2)

a = b             # rewriting variable

import math

f1 = pow(3, 2)
f2 = math.pow(3, 2)
g1 = math.sqrt(4)

h = True == False
h1 = True is False
h3 = True and False or True or False

i = 1 + 2 == 3
i1 = "string" == "string"
i2 = "string" is "string" # timdle neplest
i3 = "e" in "hello world"
i4 = "a" in "hello world"

j = "ov" + "er"
# j1 = "ov" - "o"
j2 = "repeat " + j + (" and " + j) * 10
# j3 = j / 5
j4 = "number: " + str(1)