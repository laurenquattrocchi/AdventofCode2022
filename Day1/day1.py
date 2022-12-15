# input num of calories elf is carrying
# one item caloric count per line
# elves separated by blank line
# return greatest num of calories carried

# with open('readme.txt') as f:
#     lines = f.readlines()

def max_carried_cals(input_file):

    with open(input_file) as f:
        input = f.read()

    elf_list = input.split("\n\n")

    max_cals=0
    for elf in elf_list:
        cals = elf.split("\n")
        total_cals= sum(list(map(int, cals)))
        if total_cals > max_cals:
            max_cals = total_cals

    return max_cals

#d.max_carried_cals("day1_input.txt") ans: 69795

#-----part2-----
def top3_carried_cals(input_file):

    with open(input_file) as f:
        input = f.read()

    elf_list = input.split("\n\n")

    sum_cals = []
    for elf in elf_list:
        cals = elf.split("\n")
        sum_cals.append(sum(list(map(int, cals))))
    sum_cals.sort(reverse=True)

    return sum(sum_cals[0:3])