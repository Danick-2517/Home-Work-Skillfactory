multipl = 1
n = 1
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    multipl *= n
    print(multipl)