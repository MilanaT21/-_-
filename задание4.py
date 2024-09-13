N = int(input())
total = 0
while N > 0:
    if N % 10 == 0: total += 1
    N = N // 10
print(total)
