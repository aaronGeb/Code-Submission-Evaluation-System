n = int(input())
r = []
while True:
    r.append(n)
    if n == 1:
        break
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

print(*r)