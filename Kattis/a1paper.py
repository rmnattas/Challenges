n = int(input())
p = [int(x) for x in input().split()]

p.insert(0,0)
result = 0
i_switch = False

a1_m = 2**(-(3/4))
a2_m = 2**(-(5/4))
p_measure = []
for i in range(n-1):
    if len(p_measure)%2 == 0:
        p_measure.append(a1_m)
        a1_m /= 2
    else:
        p_measure.append(a2_m)
        a2_m /= 2

print(p_measure)
#p_measure = [0.594, 0.420, 0.297, 0.210, 0.148, 0.105]
tape = 0.0
    
while True:
#    print()
#    print(1, " ", p)
    need = 1
    for i in range(n-1):
        i_switch = False 
        need -= p[i]
#        print(2, i, p, need, end=" ")

        if p[i+1]:
            if need*2 > p[i+1]:           # not enough
                switch = p[i+1]//2
                p[i] += switch
                p[i+1] -= switch * 2
                need -= switch
                for i in range(switch):
                    tape += p_measure[i]
                if switch:
                    i_switch = True
            else:                         # enough
                switch = need * 2
                p[i+1] -= switch
                p[i] += switch//2
                need -= switch//2
                for _ in range(switch//2):
                    tape += p_measure[i]
                if switch:
                    i_switch = True
        if need <= 0:
            break
        need *= 2
    if not i_switch:
        print('impossible')
        break
            
 #       print(need)
    if p[0] == 1:
        print(tape)
        break
#print()
#print(result, " ", p)

