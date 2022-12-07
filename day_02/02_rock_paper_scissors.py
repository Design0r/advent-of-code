"""--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""

"""
Points:
A/X - Rock - 1
B/Y - Paper - 2
C/Z - Scissors - 3

Lose - 0
Draw - 3
Win - 6
"""

p1_inputs = []
p2_inputs = []
with open("input.txt") as file:
    for line in file.readlines():
        p1, p2 = line.split(" ")
        p2 = p2.replace("\n", "")
        p1_inputs.append(p1)
        p2_inputs.append(p2)

def partOne():
    score = 0
    for i_1, i_2 in zip(p1_inputs, p2_inputs):
        match i_1, i_2:
            case "A", "X":
                score += 3 + 1
                print(f"Rock - Rock. Draw, 3+1 Points. Score: {score}")
            case "A", "Y":
                score += 6 + 2
                print(f"Rock - Paper. Win, 6+2 Points. Score: {score}")
            case "A", "Z":
                score += 0 + 3
                print(f"Rock - Scissors. Loss, 0+3 Points. Score: {score}")

            case "B", "X":
                score += 0 + 1
                print(f"Paper - Rock. Loss, 0+1 Points. Score: {score}")
            case "B", "Y":
                score += 3 + 2
                print(f"Paper - Paper. Draw, 3+2 Points. Score: {score}")
            case "B", "Z":
                score += 6 + 3
                print(f"Paper - Scissors. Win, 6+3 Points. Score: {score}")

            case "C", "X":
                score += 6 + 1
                print(f"Scissors - Rock. Win, 6+1 Points. Score: {score}")
            case "C", "Y":
                score += 0 + 2
                print(f"Scissors - Paper. Loss, 0+2 Points. Score: {score}")
            case "C", "Z":
                score += 3 + 3
                print(f"Scissors - Scissors. Draw, 3+3 Points. Score: {score}")

def partTwo():
    """
    X - Lose
    Y - Draw
    Z - Win
    """
    score = 0
    for i_1, i_2 in zip(p1_inputs, p2_inputs):
        match i_1, i_2:
            case "A", "X":
                score += 0 + 3
                print(f"Rock - Scissors. Loss, 0+3 Points. Score: {score}")
            case "A", "Y":
                score += 3 + 1
                print(f"Rock - Rock. Draw, 3+1 Points. Score: {score}")
            case "A", "Z":
                score += 6 + 2
                print(f"Rock - Paper. Win, 6+2 Points. Score: {score}")

            case "B", "X":
                score += 0 + 1
                print(f"Paper - Rock. Loss, 0+1 Points. Score: {score}")
            case "B", "Y":
                score += 3 + 2
                print(f"Paper - Paper. Draw, 3+2 Points. Score: {score}")
            case "B", "Z":
                score += 6 + 3
                print(f"Paper - Scissors. Win, 6+3 Points. Score: {score}")

            case "C", "X":
                score += 0 + 2
                print(f"Scissors - Paper. Loss, 0+1 Points. Score: {score}")
            case "C", "Y":
                score += 3 + 3
                print(f"Scissors - Scissors. Draw, 3+2 Points. Score: {score}")
            case "C", "Z":
                score += 6 + 1
                print(f"Scissors - Rock. Win, 6+3 Points. Score: {score}")
    print(score)





if __name__ == '__main__':
    partOne()
    partTwo()
