with open('problem2.txt') as input:
    game = [(x.split(' ')[0], x.split(' ')[1].replace('\n', '')) for x in input.readlines()]
    scores_shape = {'X':1, 'Y':2, 'Z':3}
    
    # scores for chosen shapes
    score = sum([scores_shape[x[1]] for x in game])
    # scores for outcome
    opponent = ['A', 'B', 'C']
    player = ['X', 'Y', 'Z']
    for throw in game:
        if throw[0] == opponent[(player.index(throw[1])+2)%3]:
            # win
            score += 6
        elif throw[0] == opponent[player.index(throw[1])]:
            # tie
            score += 3
        
    print('SCORE IS: ', score)

    # ============= SECOND PART ===============
    # reset score
    selected_shapes = [(player[opponent.index(x[0])], 3) if x[1]=='Y' else (player[(opponent.index(x[0])+2)%3], 0) if x[1]=='X' else (player[(opponent.index(x[0])+1)%3], 6) for x in game]
    score = sum([scores_shape[x[0]]+x[1] for x in selected_shapes])

    print("SCORE IS: ", score)