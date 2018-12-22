log_dict = {}

correct = 0
time = 0

line = input().split()
line[0] = int(line[0])

while line[0] != -1:
    if line[2] == 'wrong':
        if line[1] in log_dict:
            log_dict[line[1]] += 1
        else:
            log_dict[line[1]] = 1
    else:
        correct += 1
        time += line[0]
        if line[1] in log_dict:
            time += log_dict[line[1]]*20
    
    line = input().split()
    line[0] = int(line[0])

print(correct, time)
