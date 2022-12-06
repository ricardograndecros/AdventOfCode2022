with open('problem6.txt', 'r') as input:
    sequence = input.readline()
    marker = []
    # identify marker
    i = 0
    while len(marker) < 4 and i+3 < len(sequence):
        for j in range(0, 4):
            if len(marker) == 4:
                break
            elif sequence[i+j] not in marker:
                marker.append(sequence[i+j])
            else:
                marker = []
                break
        i+=1

    print(f'Marker {marker} found at position {i+3}')

    # =============== PART TWO =================
    # identify marker
    i = 0
    while len(marker) < 14 and i+3 < len(sequence):
        for j in range(0, 14):
            if len(marker) == 14:
                break
            elif sequence[i+j] not in marker:
                marker.append(sequence[i+j])
            else:
                marker = []
                break
        i+=1

    print(f'Marker {marker} found at position {i+13}')
        
