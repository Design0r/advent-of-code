marker_size = 14
marker = []
marker_pos = 0

with open("input.txt") as file:
    input = file.read()
    for idx, char in enumerate(input):
        if len(input[idx:idx+marker_size]) == len(set(input[idx:idx+marker_size])):
            marker.extend(input[idx:idx+marker_size])
            marker_pos = idx+marker_size
            break

print(marker, marker_pos)
