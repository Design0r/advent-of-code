"""--- Day 3: Rucksack Reorganization ---

One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

    The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
    The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
    The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
    The fourth rucksack's compartments only share item type v.
    The fifth rucksack's compartments only share item type t.
    The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""

lowerCaseAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCaseAlphabet = [x.upper() for x in lowerCaseAlphabet]


def partOne():
    comp_1, comp_2 = [], []

    with open("input.txt") as file:
        for line in file.readlines():
            comp_1.append(line[:len(line) // 2].replace("\n", ""))
            comp_2.append(line[len(line) // 2:].replace("\n", ""))

    priority = 0
    for c_1, c_2 in zip(comp_1, comp_2):
        for char in c_1:
            if char in c_1 and char in c_2:
                if char in lowerCaseAlphabet:
                    priority += lowerCaseAlphabet.index(char) + 1
                elif char in upperCaseAlphabet:
                    priority += upperCaseAlphabet.index(char) + 27
                break

    print(priority)


def partTwo():
    elf_groups = []

    with open("input.txt") as file:
        count = 0
        temp_list = []
        for line in file.readlines():
            temp_list.append(line.replace("\n", ""))
            if count >= 2:
                elf_groups.append(temp_list)
                temp_list = []
                count = 0
            else:
                count += 1

    priority = 0
    for elf_group in elf_groups:
        for item in elf_group[0]:
            if item in elf_group[0] and item in elf_group[1] and item in elf_group[2]:
                if item in lowerCaseAlphabet:
                    priority += lowerCaseAlphabet.index(item) + 1
                    print(f"lower case character: {item} with priority {lowerCaseAlphabet.index(item) + 1}, sum: {priority}")
                elif item in upperCaseAlphabet:
                    priority += upperCaseAlphabet.index(item) + 27
                    print(f"upper case character: {item} with priority {upperCaseAlphabet.index(item) + 27}, sum: {priority}")
                break


if __name__ == '__main__':
    partTwo()
