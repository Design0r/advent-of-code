import pathlib
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

with open(f"{pathlib.Path(__file__).parent}/input.txt") as file:
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


if __name__ == '__main__':
    partOne()
    partTwo()
