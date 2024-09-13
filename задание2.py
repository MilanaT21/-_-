n = int(input())
total = 1
count = 1
while count != n:
    count += 1
    total += (1 / (count ** 2))
print(total)
