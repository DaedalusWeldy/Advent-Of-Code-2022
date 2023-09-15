# Advent of Code 2022 - Day 10 Part 1
# Ah, clock speeds!

class Processor:
    def __init__(self):
        self.register = 1
        self.cycle_count = 1
        self.target_number = 20
        self.solution = 0

    def get_signal_strength(self):
        return self.cycle_count * self.register

    # If we are on cycle count 20, or on a cycle count cleanly divisible 
    # by 40, we add the current signal stregth (register * cycle_count) to
    # the 'solution' variable    
    def check_timer(self):
        if self.cycle_count == self.target_number:
            self.solution += self.get_signal_strength()
            self.target_number += 40

    def process_cycle(self, instruction):
        if instruction == "noop":
            self.cycle_count += 1
            self.check_timer()
        else:
            split_command = instruction.split()
            self.cycle_count += 1
            self.check_timer()
            self.register += int(split_command[1])
            self.cycle_count += 1
            self.check_timer()


# The actual executable portion
comm_unit = Processor()

with open("Data Files/Day 10 Data.txt", "r") as input:
    for line in input:
        x = line.strip("\n")
        comm_unit.process_cycle(line.strip("\n"))
    print("The solution is {}".format(comm_unit.solution))
