with open('problem10.txt', 'r') as input:
    commands = input.readlines()
    cycle = 0
    x = [1]*len(commands)*2
    for command in commands:
        c, v = (command.replace('\n', '').split(' ')[0], int(command.replace('\n', '').split(' ')[1])) if len(command.split(' ')) == 2 else (command.replace('\n', ''), None)
        f = False
        add_x = False
        while not f:
            if c == 'noop': # noop
                cycle += 1
                x[cycle] = x[cycle-1]
                f = True
            elif add_x: # addx v
                x[cycle] = x[cycle-1]
                add_x = False
                f = True
                cycle += 1
                x[cycle] = x[cycle-1] + v
            else: # addx
                add_x = True
                cycle += 1                

    ss = 0
    for i in range(20, 221, 40):
        ss += i*x[i-1]

    print('Signal strength: ', ss)

    # ============== PART TWO ====================
    screen = [['.']*40 for _ in range(0,6)]
    for cycle in range(0, 240):
        c = cycle % len(screen[0])
        if c in [x[cycle]-1, x[cycle], x[cycle]+1]:
            screen[int(cycle/len(screen[0]))][c] = '#'

    
    with open('problem10out.txt', 'w+') as f:
        for row in screen:
            for c in row:
                f.write(c)
            f.write('\n')