#!/usr/bin/env python3
def main() :
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority_dict = {}

    for i in range(0, 52):
        priority_dict[alphabet[i]] = i + 1

    with open("03.txt", "r") as file:
        back_packs = [entry.rstrip() for entry in file.readlines()]

    total_priority_value = 0

    for line in back_packs:
        left = line[:len(line)//2]
        right = line[len(line)//2:]
        for char in left:
            if char in right:
                total_priority_value = total_priority_value + priority_dict[char]
                break

    total_priority_value_2 = 0

    for i in range(0, len(back_packs), 3):
        first = back_packs[i]
        second = back_packs[i + 1]
        third = back_packs[i + 2]
        for char in first:
            if char in second and char in third:
                total_priority_value_2 = total_priority_value_2 + priority_dict[char]
                break

    print(f"The total priority value is {total_priority_value}")
    print(f"The total priority value of badges is {total_priority_value_2}")

if __name__ == '__main__':
    main()
