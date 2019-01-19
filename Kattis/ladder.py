import math

h, v = [int(x) for x in input().split()]
v = v * math.pi / 180
l = h / math.sin(v)

print(math.ceil(l))
