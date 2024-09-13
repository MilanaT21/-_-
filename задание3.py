N = int(input())
count = 1
total = 1
factorial = 1
while (count - 1) != N:
    total += 1 / factorial
    count += 1
    factorial *= count
print('{:.5f}'.format(total))
