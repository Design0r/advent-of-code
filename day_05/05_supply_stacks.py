import re

number_line_index = None
position_index = []
initial_state_input = []

# get input state
print("Input:")
with open("input.txt") as file:
    for idx, line in enumerate(file.readlines()):
        clean_line = line.replace("\n", "")
        initial_state_input.append(clean_line)
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

# vertical array appending
input_list = []
temp_list = []
for i, p_idx in enumerate(position_index):
    for j in range(number_line_index):
        if not initial_state_input[j][p_idx] == " ":
            temp_list.append(initial_state_input[j][p_idx])
    input_list.append(temp_list)
    temp_list = []

# shift items
with open("input.txt") as file:
    for cmd_line in file.readlines()[number_line_index+2:]:
        reg = re.findall(r"\d+", cmd_line)
        numbers = [int(x) for x in reg]

        input_list[numbers[2]-1] = (input_list[numbers[2]-1][::-1] + input_list[numbers[1]-1][:numbers[0]][::-1])[::-1]
        input_list[numbers[1]-1] = input_list[numbers[1]-1][numbers[0]:]

keyword = ""
for last_item in input_list:
    keyword += last_item[0]

print(keyword)

