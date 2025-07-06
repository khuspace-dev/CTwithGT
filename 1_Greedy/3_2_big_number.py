n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
largest = data[0]
second = data[1]

# 단순 구현

# count =  m
# result = 0

# while True:
#     for j in range(k):
#         if(count <= 0):
#             break
#         result += largest
#         count -= 1
#     if(count <= 0):
#         break
#     result += second
#     count -= 1

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * largest
result += (m - count) * second

print(result)