
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def det(A):
    result = 0

    for i in range(len(A)-1):
        result += A[i].x * A[i+1].y
    result += A[-1].x * A[0].y

    for i in range(len(A)-1):
        result -= A[i].y * A[i+1].x
    result -= A[-1].y * A[0].x

    return result/2


def main():
    n = int(input())
    for _ in range(n):
        A = []
        line = [int(x) for x in input().split()]
        for i in range(1, line[0]*2, 2):
            A.append(Point(line[i], line[i+1]))
        print(det(A))


main()
