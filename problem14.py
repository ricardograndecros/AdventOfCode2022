with open('problem14.txt', 'r') as input:
    lines = input.read().splitlines()
    sand_pouring = (500, 0)

    def parse():
        rocks = set()
        for line in lines:
            coords = [coord.split(',') for coord in line.split(' -> ')]
            for i in range(0, len(coords)-1):
                coord1, coord2 = (int(coords[i][0]), int(coords[i][1])), (int(coords[i+1][0]), int(coords[i+1][1]))
                dx = coord2[0] - coord1[0]
                dy = coord2[1] - coord1[1]
                more_rocks = [(j, coord1[1]) for j in range(coord1[0], coord2[0], int(dx/abs(dx)))] if dx != 0 else [(coord1[0], j) for j in range(coord1[1], coord2[1], int(dy/abs(dy)))]
                rocks = rocks | (set(more_rocks + [coord2]))
        return rocks


    def drop_sand(map, bounds):
        pos = sand_pouring
        sand_positioned = False
        while not sand_positioned:
            if pos[1] == bounds:
                # out of bounds!
                return (-1, -1)
            if (pos[0], pos[1]+1) in map:
                if (pos[0]-1, pos[1]+1) in map:
                    if (pos[0]+1, pos[1]+1) in map:
                        sand_positioned = True # flat
                    else:
                        pos = (pos[0]+1, pos[1]+1) # bottom right
                else:
                    pos = (pos[0]-1, pos[1]+1) # bottom left
            else:
                pos = (pos[0], pos[1]+1)
        
        return pos

    rocks = parse()
    map_bounds = max(rocks, key=lambda x:x[1])[1]
    is_sand_falling = False
    total_sand = 0
    while not is_sand_falling:
        current_pos = drop_sand(rocks, map_bounds)
        if current_pos == (-1, -1):
            is_sand_falling = True
        else: 
            total_sand += 1
            rocks.add(current_pos)

    print(total_sand)

    # =============== PART TWO ===============
    def drop_sand(map, bounds):
        pos = sand_pouring
        sand_positioned = False
        while not sand_positioned:
            if pos[1] + 1 == bounds + 2:
                # floor reached!
                sand_positioned = True
                break
            if (pos[0], pos[1]+1) in map:
                if (pos[0]-1, pos[1]+1) in map:
                    if (pos[0]+1, pos[1]+1) in map:
                        sand_positioned = True # flat
                    else:
                        pos = (pos[0]+1, pos[1]+1) # bottom right
                else:
                    pos = (pos[0]-1, pos[1]+1) # bottom left
            else:
                pos = (pos[0], pos[1]+1)
        
        return pos


    def print_map(rocks):
        map = [['.']*20 for _ in range(0, 12)]
        for i in range(0, 12):
            for j in range(490, 510):
                map[i][j-490] = 'o' if (j,i) in rocks else '.'

        for row in map:
            print(''.join(row))


    rocks = parse()
    is_map_full = False
    total_sand = 0
    while not is_map_full:
        current_pos = drop_sand(rocks, map_bounds)
        if current_pos == sand_pouring:
            is_map_full = True
        else: 
            rocks.add(current_pos)
        total_sand += 1
        # print_map(rocks) # for animation

        


    print(total_sand)
    
            