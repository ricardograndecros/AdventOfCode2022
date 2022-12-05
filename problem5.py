with open('problem5.txt') as input:
    lines = input.readlines()
    # get stacks of crates
    storage = [[] for i in range(0,9)]
    for i in range(0, 8):
        row = [lines[i][j:j+3] for j in range(0, len(lines[i]), 4)]
        for k in range(0,9):
            if row[k].replace(' ', '') != '':
                storage[k].append(row[k].replace('[', '').replace(']', ''))
    
    # process instructions
    for line in lines[10:]:
        s1, n, s2, origin, s3, dest = line.split(' ')
        for i in range(0,int(n)):
            crate = storage[int(origin)-1].pop(0)
            storage[int(dest)-1].insert(0, crate)

    print([storage[i][0] for i in range(0,9)])

    # ============= PART TWO ==============
    # get stacks of crates
    storage = [[] for i in range(0,9)]
    for i in range(0, 8):
        row = [lines[i][j:j+3] for j in range(0, len(lines[i]), 4)]
        for k in range(0,9):
            if row[k].replace(' ', '') != '':
                storage[k].append(row[k].replace('[', '').replace(']', ''))
    
    # process instructions
    for line in lines[10:]:
        s1, n, s2, origin, s3, dest = line.split(' ')
        crates = [storage[int(origin)-1].pop(0) for i in range(0,int(n))]
        for crate in reversed(crates):
            storage[int(dest)-1].insert(0, crate)

    print([storage[i][0] for i in range(0,9)])



            