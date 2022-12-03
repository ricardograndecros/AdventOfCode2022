with open('problem3.txt', 'r') as input:
    backpacks = [backpack.replace('\n', '') for backpack in input.readlines()]
    first, second = zip(*[(backpack[:len(backpack)//2], backpack[len(backpack)//2:]) for backpack in backpacks])
    # find the misplaced item
    misplaced = []
    for comp1, comp2 in zip(first, second):
        misplaced += set(comp1).intersection(set(comp2))
    # calculate sum
    sum = 0
    for c in misplaced:
        c = ord(c)
        if c>=65 and c<=90:
            # uppercase
            sum += c-38 # A:65 (ascii), 65-38=27
        elif c>=97 and c<=122:
            sum += c-96 # a:97 (ascii), 97-96=1
    print("Total sum of misplaced priorities: ", sum)

    # ============ SECOND PART ================
    # split backpacks in groups of three
    badges = []
    for i in range(0, len(backpacks), 3):
        badges += (set(backpacks[i]).intersection(set(backpacks[i+1]))).intersection(set(backpacks[i+2]))
    
    sum=0
    for c in badges:
        c = ord(c)
        if c>=65 and c<=90:
            # uppercase
            sum += c-38 # A:65 (ascii), 65-38=27
        elif c>=97 and c<=122:
            sum += c-96 # a:97 (ascii), 97-96=1
    print("Total sum of badges priorities: ", sum)