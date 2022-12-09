import math

with open('problem9.txt', 'r') as input:
    visited = []
    head = (0, 0)
    tail = (0, 0)
    moves = input.readlines()
    for move in moves:
        dir, steps = move.split(' ')
        steps = int(steps)
        for i in range(0, steps):
            # head move
            if dir == 'U':
                head = (head[0], head[1] + 1)
            elif dir == 'D':
                head = (head[0], head[1] - 1)
            elif dir == 'R':
                head = (head[0] + 1, head[1])
            elif dir == 'L':
                head = (head[0] - 1, head[1])
            # tail move
            # move only if distance > 1
            if head[0] - tail[0] > 1:
                # move tail right
                tail = (tail[0] + 1, head[1])
            elif tail[0] - head[0] > 1:
                # move tail left
                tail = (tail[0] - 1, head[1])
            # different if statement to allow diagonal moves
            if head[1] - tail[1] > 1:
                # move tail up
                tail = (head[0], tail[1] + 1)
            elif tail[1] - head[1] > 1:
                # move tail down
                tail = (head[0], tail[1] - 1)

            visited.append(tail)

    print(f'The tail visited {len(set(visited))} different positions')


    # ======== PART TWO ================
    visited = []
    knots = [(0,0)]*10
    for move in moves:
        dir, steps = move.split(' ')
        steps = int(steps)
        for i in range(0, steps):
            # head move
            if dir == 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif dir == 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif dir == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif dir == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            # knots move
            for k in range(1, len(knots)):
                # move only if distance > 1
                if math.sqrt((knots[k-1][0]-knots[k][0])**2+(knots[k-1][1]-knots[k][1])**2) > 2:
                    # new case
                    m_x = math.copysign(1, (knots[k-1][0]-knots[k][0]))
                    m_y = math.copysign(1, (knots[k-1][1]-knots[k][1]))
                    knots[k] = (knots[k][0] + int(m_x), knots[k][1] + int(m_y))
                else:
                    if knots[k-1][0] - knots[k][0] > 1:
                        # move right
                        knots[k] = (knots[k][0] + 1, knots[k-1][1])
                    elif knots[k][0] - knots[k-1][0] > 1:
                        # move left
                        knots[k] = (knots[k][0] - 1, knots[k-1][1])
                    # different if statement to allow diagonal moves
                    if knots[k-1][1] - knots[k][1] > 1:
                        # move up
                        knots[k] = (knots[k-1][0], knots[k][1] + 1)
                    elif knots[k][1] - knots[k-1][1] > 1:
                        # move down
                        knots[k] = (knots[k-1][0], knots[k][1] - 1)

            visited.append(knots[-1])
    

    print(f'The tail visited {len(set(visited))} different positions')
    
