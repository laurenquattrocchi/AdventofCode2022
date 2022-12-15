# A for Rock, B for Paper, and C for Scissors 
# X for Rock, Y for Paper, and Z for Scissors
# The score 1 for Rock, 2 for Paper, and 3 for Scissors
# plus 0 if you lost, 3 if the round was a draw, and 6 if you won

PLAYS = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

def total_score(input_file):
    with open(input_file) as f:
        strategy = f.readlines()

    score = 0
    for round in strategy:
        if PLAYS[round[0]] ==  PLAYS[round[2]]:
            # tie
            score = score + PLAYS[round[2]] + 3
        elif round[0] == 'A':
            if round[2] == 'Y':
                # you win
                score = score + PLAYS[round[2]] + 6
            if round[2] == 'Z':
                # you lose
                score = score + PLAYS[round[2]]
        elif round[0] == 'B':
            if round[2] == 'Z':
                # you win
                score = score + PLAYS[round[2]] + 6
            if round[2] == 'X':
                # you lose
                score = score + PLAYS[round[2]]
        elif round[0] == 'C':
            if round[2] == 'X':
                # you win
                score = score + PLAYS[round[2]] + 6
            if round[2] == 'Y':
                # you lose
                score = score + PLAYS[round[2]]
        
    return score
#d.total_score("input.txt") answ: 13924

#--------PART 2-----------------#
# X you need to lose, Y you need to draw, and Z you need to win
def move(input_file):
    with open(input_file) as f:
        strategy = f.readlines()
    
    score = 0
    for round in strategy:
        if round[0] == 'A':
            if round[2] == 'X':
                score = score + 3 # 3 for sissor, 0 for losing
            if round[2] == 'Y':
                score = score + 4 # 1 for rock, 3 for draw
            if round[2] == 'Z':
                score = score + 8 # 2 for paper 6 for win
        elif round[0] == 'B':
            if round[2] == 'X':
                score = score + 1 # 1 for rock, 0 for losing
            if round[2] == 'Y':
                score = score + 5 # 2 for paper, 3 for draw
            if round[2] == 'Z':
                score = score + 9 # 3 for scissor 6 for win
        elif round[0] == 'C':
            if round[2] == 'X':
                score = score + 2 # 2 for paper, 0 for losing
            if round[2] == 'Y':
                score = score + 6 # 3 for scissor , 3 for draw
            if round[2] == 'Z':
                score = score + 7 # 1 for rock,  6 for win
    return score
        
# d.move("input.txt") 13448

