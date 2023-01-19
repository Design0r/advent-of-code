import time


def moveTail(tail_knots):
    for idx, knot in enumerate(tail_knots):
        if idx == 0:
            col_diff = head_pos_col - knot[1]
            row_diff = head_pos_row - knot[0]
        else:
            col_diff = tail_knots[idx-1][1] - knot[1]
            row_diff = tail_knots[idx-1][0] - knot[0]

        if abs(col_diff) >= 2 and abs(row_diff) == 0:
            knot[1] += 1 if col_diff >= 0 else -1

        elif abs(row_diff) >= 2 and abs(col_diff) == 0:
            knot[0] -= 1 if row_diff <= 0 else -1

        elif abs(row_diff) >= 2 and abs(col_diff) >= 1:
            knot[0] -= 1 if row_diff <= 0 else -1
            knot[1] += 1 if col_diff >= 0 else -1

        elif abs(col_diff) >= 2 and abs(row_diff) >= 1:
            knot[1] += 1 if col_diff >= 0 else -1
            knot[0] -= 1 if row_diff <= 0 else -1

    setTail(tail_knots[-1])


def setTail(knot_pos):
    grid[knot_pos[0]][knot_pos[1]] = "T"


def createTailKnots(num, pos):
    temp = []
    for i in range(num):
        temp.append(pos)

    return temp


def getTailCount():
    count = 0
    for i in grid:
        for j in i:
            count += 1 if j == "T" else 0
    return count


if __name__ == '__main__':
    start_time = time.time()

    grid_size = 500
    grid = [["." for j in range(grid_size)] for i in range(grid_size)]

    head_pos_row = 5
    head_pos_col = 0
    knot_count = 9
    tail_knots = [[head_pos_row, head_pos_col].copy() for i in range(knot_count)]

    file = open("input.txt").read().split("\n")
    for line in file:
        num = int(line.split(" ")[1])
        match line.split(" ")[0]:
            case "R":
                for i in range(num):
                    head_pos_col += 1
                    moveTail(tail_knots)
            case "L":
                for i in range(num):
                    head_pos_col -= 1
                    moveTail(tail_knots)
            case "U":
                for i in range(num):
                    head_pos_row -= 1
                    moveTail(tail_knots)
            case "D":
                for i in range(num):
                    head_pos_row += 1
                    moveTail(tail_knots)
    print(f"tail count: {getTailCount()}, found in {time.time()-start_time}s")
