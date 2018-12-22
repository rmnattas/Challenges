m = input()
temps = [int(x) for x in input().split()]

result = 0
for temp in temps:
    if temp < 0:
        result += 1

print(result)
