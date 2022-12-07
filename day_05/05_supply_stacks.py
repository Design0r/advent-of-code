number_line_index = None
position_index = []
clean_input = []

print("Input:")
with open("input.txt") as file:
    for idx, line in enumerate(file.readlines()):
        clean_line = line.replace("\n", "")
        clean_input.append(clean_line)
        print(clean_line)

        is_number_line = False
        for char in clean_line:
            try:
                if isinstance(int(char), int):
                    position_index.append(clean_line.index(char))
                    is_number_line = True
                    number_line_index = idx
                else:
                    is_number_line = False
            except:
                pass
        if is_number_line is True:
            break

input_list = []

"""
# horizontal appending
for idx, line in enumerate(clean_input):
    temp_list = []
    if idx >= number_line_index:
        break

    for p_idx in position_index:
        if p_idx > len(line):
            temp_list.append(" ")
            break
        else:
            temp_list.append(line[p_idx])

    input_list.append(temp_list)"""

# vertical appending
temp_list = []
for i, p_idx in enumerate(position_index):
    for j in range(number_line_index):
        temp_list.append(clean_input[j][p_idx])
    input_list.append(temp_list)
    temp_list = []

print("\nRebuilt Array:")
for i in reversed(input_list): print(i)
