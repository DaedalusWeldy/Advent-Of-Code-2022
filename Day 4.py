# Advent of Code 2022 - Day 4
# Cleaning areas

class NumberRange:
    def __init__(self, min_input = 0, max_input = 0):
        self.minimum_value = min_input
        self.maximum_value = max_input

    def translateRangeData(self, range_data_input):
        split_data = range_data_input.split("-")
        self.minimum_value = int(split_data[0])
        self.maximum_value = int(split_data[1])

    def isNumberInRange(self, number_to_check):
        if number_to_check >= self.minimum_value and number_to_check <= self.maximum_value:
            return True
        else:
            return False
    
    #43-65, 5-43 returns True. WHY?!
    def containsRange(self, range_to_test):
        if range_to_test.minimum_value >= self.minimum_value and range_to_test.maximum_value <= self.maximum_value:
            return True
        else:
            return False
        
    def doesRangeOverlap(self, range_to_test):
        range_numbers = [*range(self.minimum_value, self.maximum_value + 1)]
        print(range_numbers)
        test_numbers = [*range(range_to_test.minimum_value, range_to_test.maximum_value + 1)]
        print(test_numbers)
        overlap = False
        for entry in test_numbers:
            if range_numbers.count(entry) > 0:
                overlap = True
                break
        return overlap
        
    def printRange(self):
        return ("{0}-{1}".format(self.minimum_value, self.maximum_value))
    
    
with open("Data Files/Day 4 Data.txt", "r") as file_input:
    total_overlaps = 0
    partial_overlaps = 0
    elf_a = NumberRange()
    elf_b = NumberRange()
    for entry in file_input:
        pair_of_elves = entry.split(",")

        elf_a.translateRangeData(pair_of_elves[0])
        elf_b.translateRangeData(pair_of_elves[1])
        
        if elf_a.containsRange(elf_b) or elf_b.containsRange(elf_a):
            total_overlaps += 1
        
        if elf_a.doesRangeOverlap(elf_b):
            partial_overlaps += 1
    print("Total number of complete overlaps is " + str(total_overlaps))
    print("Total number of partial overlaps is " + str(partial_overlaps))


