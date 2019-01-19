
import math



def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def vecSub(a, b):
    return [ (a[0]-b[0]) , (a[1]-b[1]) , (a[2]-b[2]) ]




def main():
    k, m = [int(x) for x in input().split()]

    while k or m:
        sats = []
        tars = []

        for _ in range(k):
            sats.append([float(x) for x in input().split()])

        for _ in range(m):
            tars.append([float(x) for x in input().split()])

        total = 0

        for tar in tars:
            for sat in sats:
                ts = vecSub(sat, tar)
                ang = angle(tar, ts)
                if ang < math.pi/2 :
                    total += 1
                    break

        print(total)

        
        k, m = [int(x) for x in input().split()]

main()
