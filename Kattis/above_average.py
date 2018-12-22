m = int(input())

clss = []
for _ in range(m):
    clss.append([int(x) for x in input().split()][1:])

for cls in clss:
    avg = 0
    above_avg = 0
    for student in cls:
        avg += student
    avg /= len(cls)
    for student in cls:
        if student > avg:
            above_avg += 1
    print("%.3f%%" % (round((above_avg/len(cls)*100),3)))


