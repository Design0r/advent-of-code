from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_15.txt").read().strip()


class Lens:
    __slots__ = ("label", "_focal_length")

    def __init__(self, label: str, focal: str | int):
        self.label = label

        if not isinstance(focal, int):
            self._focal_length = int(focal)
            return

        self._focal_length = focal

    @property
    def focal_length(self):
        return self._focal_length

    @focal_length.setter
    def focal_length(self, value):
        if not isinstance(value, int):
            self._focal_length = int(value)
            return
        self._focal_length = value

    def __eq__(self, __value: object) -> bool:
        return self.label == __value.label


def to_hash(input: str) -> int:
    value = 0
    for c in input:
        ascii = ord(c)
        value += ascii
        value *= 17
        value %= 256

    return value


def part_1():
    result = sum(map(to_hash, file.split(",")))
    print("Day 15, Part 1:", result)


def parse_cmd(input: str) -> dict[str, int]:
    if "=" in input:
        label, num = input.split("=")
        return {label: int(num)}

    label, num = input.split("-")
    return {label: int(num)}


def part_2():
    boxes: dict[int, list[Lens]] = {}
    for cmd in file.split(","):
        if "=" in cmd:
            label, num = cmd.split("=")
            hashed = to_hash(label)
            lens = Lens(label, num)
            if not boxes.get(hashed):
                boxes[hashed] = [lens]
                continue

            lens_list = boxes[hashed]
            if lens not in lens_list:
                lens_list.append(lens)
                continue

            index = lens_list.index(lens)
            lens_list[index].focal_length = num
            continue

        label = cmd.split("-")[0]
        lens = Lens(label, 0)
        hashed = to_hash(label)
        lens_list = boxes.get(hashed)
        if not lens_list:
            continue
        if lens not in lens_list:
            continue
        lens_list.remove(lens)
        boxes[hashed] = lens_list

    result = sum(
        (1 + box) * idx * lens.focal_length
        for box, lenses in boxes.items()
        for idx, lens in enumerate(lenses, 1)
    )
    print("Day 15, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
