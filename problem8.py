with open('problem8.txt', 'r') as input:
    lines = input.readlines()
    grid = [[0]*(len(lines[0])-1) for _ in range(0, len(lines))]
    for row in range(0, len(lines)):
        for column in range(0, len(lines[row][:-1])): # -1 to skip /n
            grid[row][column] = int(lines[row][column])
    
    visible_trees = [[True]*(len(lines[0])-1) for _ in range(0, len(lines))]
    count_visible_trees = 0
    for row in range(1, len(grid[:-1])): # -1 to skip edges
        for column in range(1, len(grid[row][:-1])): # -1 to skip edges
            is_visible_top = True if grid[row][column] > max([grid[i][column] for i in range(row-1, -1, -1)]) else False
            is_visible_bot = True if grid[row][column] > max([grid[i][column] for i in range(row+1, len(grid))]) else False
            is_visible_left = True if grid[row][column] > max([grid[row][i] for i in range(column-1, -1, -1)]) else False
            is_visible_right = True if grid[row][column] > max([grid[row][i] for i in range(column+1, len(grid[row]))]) else False
            visible_trees[row][column] = is_visible_top or is_visible_bot or is_visible_left or is_visible_right

    print(f"There are {sum(sum(visible_trees, []))} visible trees")

    # =========== PART TWO =================
    scenic_score = [[0]*(len(lines[0])-1) for _ in range(0, len(lines))]
    for row in range(1, len(grid[:-1])): # -1 to skip edges
        for column in range(1, len(grid[row][:-1])): # -1 to skip edges
            top = 0
            bot = 0
            left = 0
            right = 0
            # check up
            for i in range(row-1, -1, -1):
                top += 1
                if grid[i][column] >= grid[row][column]:
                    break
            # check bottom
            for i in range(row+1, len(grid)):
                bot += 1
                if grid[i][column] >= grid[row][column]:
                    break
            # check left
            for i in range(column-1, -1, -1):
                left += 1
                if grid[row][i] >= grid[row][column]:
                    break
            # check right
            for i in range(column+1, len(grid[row])):
                right += 1
                if grid[row][i] >= grid[row][column]:
                    break     

            scenic_score[row][column] = top*bot*left*right           

    print(f'Max scenic score is {max(map(max, scenic_score))}')
