m = int(input())
books = []

for _ in range(m):
    books.append(int(input()))

books = sorted(books, reverse=True)
price = 0

group_i = 0
for i in range(len(books)):
    if group_i != 2:
        price += books[i]
        group_i += 1
    else:
        group_i = 0

print(price)
