N = int(input())

count = 0

for hour in range(0, N + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if("3" in str(second)):
                count += 1
                continue
            if("3" in str(minute)):
                count += 1
                continue
            if("3" in str(hour)):
                count += 1
                continue

print(count)