n = 1260
count = 0

units = [ 500, 100, 50, 10 ]

for unit in units:
    count += n // unit
    n %= unit

print(count)