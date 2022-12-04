#!/usr/bin/env python3
def main() :
    with open("01.txt", "r") as file:
        elf_list = sorted(\
            [sum([int(calorie) for calorie in elf]) \
            for elf in [elf.split('\n') for elf in file.read().rstrip().split('\n\n')]]\
            , reverse=True)

    print(f'Elf with most calories carries {elf_list[0]} calories')
    print(f'The three carrying most calories carries {sum(elf_list[0:3])} calories')

if __name__ == '__main__':
    main()
