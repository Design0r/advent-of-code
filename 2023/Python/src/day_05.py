from pathlib import Path

file = open(Path(__file__).parent.parent / "samples/day_05.txt").read()
seeds = map(lambda x: int(x), file.split("\n")[0].split(": ")[1].split(" "))

maps = file.split("\n\n")
for map in maps:
    map = map.split("\n")
    map.pop(0)

    rows = [(j) for i in map for j in i.split("\n")]
    map_values = [(j[0], j[1], j[2]) for i in rows for j in i.split(" ")]
    print(map_values, "\n")
