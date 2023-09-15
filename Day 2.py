# Day 2 of the Advent of Code 2022 challenge
# "Rock, Paper, Scissors Tournament"

# Method for calculating score for a given round
# your_play should be A, B or C (code for Rock, Paper or Scissors)
# opponent_play should be X, Y or Z (also code for Rock, Paper or Scissors)
def calculateRound(line_input):
    # Parse the string and remove both your play and the opponent's play
    your_play = line_input[2].upper()
    opponent_play = line_input[0].upper()
    total_score = 0
    result = ""

    # Register score for the sign you played
    if your_play == 'X':
        total_score += 1
    elif your_play == 'Y':
        total_score += 2
    elif your_play == 'Z':
        total_score += 3
    # Register the result of the round (points for win or draw, none for loss)
    if your_play == 'X':
        if opponent_play == 'A':
            total_score += 3
        elif opponent_play == 'C':
            total_score += 6
    elif your_play == 'Y':
        if opponent_play == 'B':
            total_score += 3
        elif opponent_play == 'A':
            total_score += 6
    elif your_play == 'Z':
        if opponent_play == 'C':
            total_score += 3
        elif opponent_play == 'B':
            total_score += 6
    else:
        print("ERROR: Not a valid input")
    return total_score

def calculateAlternateRound(file_input):
    opponent_play = file_input[0].upper()
    # For desired_outcome, X means lose, Y means draw and Z means win
    desired_outcome = file_input[2].upper()
    your_play = ""

    if desired_outcome == 'Y': # Draw
        if opponent_play == 'A':
            your_play = 'X'
        elif opponent_play == 'B':
            your_play = 'Y'
        elif opponent_play == 'C':
            your_play = 'Z'
    elif desired_outcome == 'X': # Lose
        if opponent_play == 'A':
            your_play = 'Z'
        elif opponent_play == 'B':
            your_play = 'X'
        elif opponent_play == 'C':
            your_play = 'Y'
    elif desired_outcome == 'Z': # Win
        if opponent_play == 'A':
            your_play = 'Y'
        elif opponent_play == 'B':
            your_play = 'Z'
        elif opponent_play == 'C':
            your_play = 'X'
    round_matchup = opponent_play + " " + your_play
    return calculateRound(round_matchup)


with open("Data Files/Day 2 Data.txt", "r") as file_input:
    tournament_score = 0
    for entry in file_input:
        tournament_score = tournament_score + calculateAlternateRound(entry)
    print(tournament_score)