#!/usr/bin/env python3
def main() :
    scoring_dict = {
        "AX" : 4,
        "AY" : 8,
        "AZ" : 3,
        "BX" : 1,
        "BY" : 5,
        "BZ" : 9,
        "CX" : 7,
        "CY" : 2,
        "CZ" : 6
    }

    translation_dict = {
        "AX" : "AZ",
        "AY" : "AX",
        "AZ" : "AY",
        "BX" : "BX",
        "BY" : "BY",
        "BZ" : "BZ",
        "CX" : "CY",
        "CY" : "CZ",
        "CZ" : "CX"
    }

    with open("02.txt") as file:
        matches_list = file.read().replace(' ', '').rstrip().split('\n')

    my_score = 0

    for match in matches_list:
        my_score = my_score + scoring_dict[match]

    my_score_2 = 0
    for match in matches_list:
        my_score_2 = my_score_2 + scoring_dict[translation_dict[match]]

    print(f"My score according to the first way to calculate: {my_score}")

    print(f"My score according to the second way to calculate: {my_score_2}")


if __name__ == '__main__':
    main()
