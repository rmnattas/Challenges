s = int(input())
while s:
    if s == 1:
        print(1)
    else:
        print(2*(s-1))
    try:
        s=int(input())
    except:
        break
