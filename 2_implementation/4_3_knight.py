point = input()

board = ['','a','b','c','d','e','f','g','h']

x = int(board.index(point[0]))
y = int(point[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
count = 0
for step in steps:
    step_x = x + step[0]
    step_y = y + step[1]
    print(step_x, step_y)
    if step_x > 0 and step_y > 0 and step_x < 9 and step_y < 9:
        count += 1

print(count)