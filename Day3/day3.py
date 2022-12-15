priority = {
    "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
    "i": 9,"j":10, "k": 11, "l":12, "m":13, "n":14, "o":15,
    "p":16,"q":17, "r":18, "s":19, "t":20, "u":21, "v":22,
    "w":23,"x":24, "y":25, "z":26, "A":27, "B":28, "C":29, 
    "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
    "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43,
    "R":44, "S":45,  "T":46, "U":47, "V":48, "W":49, "X":50,
    "Y":51, "Z":52
    }

def contents(input_file):
    with open(input_file) as f:
        rucksacks = f.read().splitlines()
    
    p_sum = 0
    for rucksack in rucksacks:
        mid = int(len(rucksack)/2)
        comp1 = rucksack[0:mid]
        comp2 = rucksack[mid:]
        for item in comp1:
            if item in comp2:
                p_sum = p_sum + priority[item]
    
    return p_sum

#---------------part 2-------------------------#

def badge(input_file):
    with open(input_file) as f:
    with open("input.txt") as f:
        rucksacks = f.read().splitlines()
    
    p_sum = 0
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i : i + 3]
        for item in group[0]:
            if item in group[1] and item in group[2]:
                print (item)
                print('group num', i, "-", i+3)
                p_sum = p_sum + priority[item]
                break   # added in so don't keep checking after find match - ideally would get same answer
                        # w/o this but I am finding more then one match per group in input file

    
    return p_sum
