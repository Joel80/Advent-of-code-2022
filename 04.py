#!/usr/bin/env python3
def main() :
    with open("04.txt", "r") as file:
        pair_list = [x.split(',') for x in file.read().rstrip().split('\n')]
    
    def isSubRange(range1, range2):
        if int(range1[0]) >= int(range2[0]):
            if int(range1[1]) <= int(range2[1]):
                return True
        return False

    def isOverlapping(range1, range2):
        if int(range1[1]) <= int(range2[1]):
            if int(range1[1]) >= int(range2[0]):
                return True
        elif int(range1[0]) >= int(range2[0]):
            if int(range1[0]) <= int(range2[1]):
                return True
        return False

    count_pairs_fully_contained = 0

    count_pairs_overlapping = 0

    for pair in pair_list:
        ranges = [pair[0].split('-'), pair[1].split('-')]

        if isSubRange(ranges[0], ranges[1]):
            count_pairs_fully_contained = count_pairs_fully_contained + 1
        elif isSubRange(ranges[1], ranges[0]): 
            count_pairs_fully_contained = count_pairs_fully_contained + 1

        if isOverlapping(ranges[0], ranges[1]):
            count_pairs_overlapping = count_pairs_overlapping + 1
        elif isOverlapping(ranges[1], ranges[0]):
            count_pairs_overlapping = count_pairs_overlapping + 1

    print(f"Nr of pairs where one fully contains the other: {count_pairs_fully_contained}")
    print(f"Nr of pairs overlapping: {count_pairs_overlapping}")

if __name__ == '__main__':
    main()
