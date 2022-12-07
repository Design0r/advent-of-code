def main():
    with open("input.txt") as file:
        # foreach row
        total_count = 0
        partial_count = 0
         
        for line in file.read().split("\n"):
            a1, a2, b1, b2 = map(int, line.replace(",", "-").split("-"))

            partial_count += 1 if a1 <= b1 <= a2 or b1 <= a1 <= b2 else 0
            # partial_count += 1 if not (a2 < b1 or a1 > b2) else 0
            
            if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
                total_count += 1

        print(partial_count)

main()