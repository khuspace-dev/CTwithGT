N, M = map(int, input().split())
x, y, direction = map(int, input().split())

board = []
steps = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

for i in range(N):
    board.append(list(map(int, input().split())))

flag = True
count = 1
while(flag):
    board[x][y] = 2
    for _ in range(4):
        direction = (direction + 3) % 4
        next_x = x + steps[direction][0]
        next_y = y + steps[direction][1]
        if(board[next_x][next_y] == 0):
            x = next_x
            y = next_y
            count += 1
            break
        
        # 4번 다 돌아야 발동
        if(i == 3) :
            post_x = x - steps[direction][0]
            post_y = y - steps[direction][1]
            # 뒤가 땅이면 후진
            if (board[post_x][post_y] == 2):
                x = post_x
                y = post_y
                break
            # 뒤가 바다면 정지
            else:
                flag = False
                
print(count)


    

