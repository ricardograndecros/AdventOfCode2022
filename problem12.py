with open('problem12.txt', 'r') as input:
    lines = [line.replace('\n', '') for line in input.readlines()]
    map = [[0]*len(lines[0]) for _ in range(0, len(lines))]
    start = (0, 0)
    start_list = [] # for part 2
    end = (0, 0)
    for row in range(0, len(lines)):
        for column in range(0, len(lines[0])):
            if lines[row][column] == 'S':
                start = (row, column)
                start_list.append((row, column))
            elif lines[row][column] == 'E':
                end = (row, column)
            else:
                # convert chars to integers
                if lines[row][column] == 'a':
                    start_list.append((row, column))
                map[row][column] = ord(lines[row][column]) - 97 # a = 0
    
    map[start[0]][start[1]] = 0
    map[end[0]][end[1]] = ord('z') - 97

    # Dijkstra algorithm
    def dijkstra(map, start, part):
        distances = [[float('inf')]*len(map[0]) for _ in range(0, len(map))]
        distances[start[0]][start[1]] = 0 # set distance to start point to 0

        visited = [] # visited nodes

        queue = []
        queue.append((0, start))

        while len(queue) > 0:
            d, curr_node = queue.pop(0)
            visited.append(curr_node)

            # get adjacent nodes
            neighbors = []
            if curr_node[0]+1 < len(map):
                if map[curr_node[0]][curr_node[1]] - map[curr_node[0]+1][curr_node[1]] >= -1 and part==1 or\
                    map[curr_node[0]][curr_node[1]] - map[curr_node[0]+1][curr_node[1]] <= 1 and part==2:
                    neighbors.append((curr_node[0]+1, curr_node[1]))
            if curr_node[0]-1 >= 0:
                if map[curr_node[0]][curr_node[1]] - map[curr_node[0]-1][curr_node[1]] >= -1 and part == 1 or\
                    map[curr_node[0]][curr_node[1]] - map[curr_node[0]-1][curr_node[1]] <= 1 and part==2:
                    neighbors.append((curr_node[0]-1, curr_node[1]))
            if curr_node[1]+1 < len(map[0]):
                if map[curr_node[0]][curr_node[1]] - map[curr_node[0]][curr_node[1]+1] >= -1 and part == 1 or\
                    map[curr_node[0]][curr_node[1]] - map[curr_node[0]][curr_node[1]+1] <= 1 and part==2:
                    neighbors.append((curr_node[0], curr_node[1]+1))
            if curr_node[1]-1 >= 0:
                if map[curr_node[0]][curr_node[1]] - map[curr_node[0]][curr_node[1]-1] >= -1 and part == 1 or\
                    map[curr_node[0]][curr_node[1]] - map[curr_node[0]][curr_node[1]-1] <= 1 and part==2:
                    neighbors.append((curr_node[0], curr_node[1]-1))
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    old_cost = distances[neighbor[0]][neighbor[1]]
                    new_cost = distances[curr_node[0]][curr_node[1]] + 1
                    if new_cost < old_cost:
                        queue.append((new_cost, neighbor))
                        distances[neighbor[0]][neighbor[1]] = new_cost

            queue.sort(key=lambda node: node[0])
        
        return distances
            


    distances = dijkstra(map, start, 1)

    print(f"Shortest path to {end} = {distances[end[0]][end[1]]}")

    # ======= PART TWO ==========
    distances = dijkstra(map, end, 2)
    shortest_paths = [distances[start[0]][start[1]] for start in start_list]
    print(f"Shortest path from 'a' altitude is {min(shortest_paths)} steps")

    
