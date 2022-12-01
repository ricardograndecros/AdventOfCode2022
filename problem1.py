import requests

with open('./problem1.txt', 'r') as input:
    # separate array by \n
    curr_elf = 0
    elfs = {0:[]}
    for food in input.readlines():
        if food == '\n':
            curr_elf+=1
            elfs[curr_elf] = []
            continue
        elfs[curr_elf].append(int(food))
    # ====== PART 1 ====================
    # get highest
    max_elf = None
    max_food = 0
    for elf in elfs.keys():
        if sum(elfs[elf]) > max_food:
            max_food = sum(elfs[elf])
            max_elf = elf
    
    print(f"Solutoin problem 1: Elf carrying the most food: {max_elf}, most food carried: {max_food}")

    # ====== PART 2 ===================
    sorted_elfs = [sorted(elfs.items(), key=lambda item: sum(item[1]))]
    total_food = [sum(x[1]) for x in sorted_elfs[0][-3:]]
    print(sorted_elfs[0][-3:])
    print(f"Best three elfs have {sum(total_food)} food")