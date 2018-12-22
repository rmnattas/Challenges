m = int(input())
line = [int(x) for x in input().split()]

dic = {}
highest = 0
winner = "none"

for i in range(m):
    if line[i] not in dic:
        dic[line[i]] = 1
    else:
        dic[line[i]] += 1

for player in dic.keys():
    if dic[player] == 1:
        if player > highest:
            highest = player
            winner = line.index(player)+1

print(winner)
    
