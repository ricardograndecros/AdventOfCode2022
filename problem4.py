with open('problem4.txt') as input:
    elfs = [section.replace('\n', '').split(',') for section in input.readlines()]
    section1, section2 = zip(*[((section[0].split('-')),(section[1].split('-'))) for section in elfs])
    
    contained = 0
    for elf1, elf2 in zip(section1, section2):
        if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])) or \
            (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
            contained+=1

    print(contained)

    # ============ PART TWO ===================
    overlapped = 0
    for elf1, elf2 in zip(section1, section2):
        if int(elf1[1])>= int(elf2[0]) and int(elf2[1]) >= int(elf1[1]) or \
            int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[1]):
            overlapped+=1

    print(overlapped)