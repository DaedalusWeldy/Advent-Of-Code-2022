# Advent of Code 2022 - Day 10 Part 2
# Now CRT displays?!
# Note: Fix offset on display; first column missing, one extra
# column at the end.

class Processor:
    def __init__(self):
        self.register = 1
        self.cycle_count = 1
        self.line_count = 0
        self.display = ["","","","","",""]

    def within_cursor_range(self, pos_to_check):
        if (abs(self.register - pos_to_check) > 1):
            return False
        else:
            return True
        
    def update_display_line(self, line):
        if self.within_cursor_range(self.cycle_count):
            self.display[line] = self.display[line] + "#"
        else:
            self.display[line] = self.display[line] + "."

    def update_cycle_count(self):
        divided_count = divmod(self.cycle_count, 40)
        self.cycle_count += 1
        if divided_count[1] == 0:
            self.line_count += 1
            self.cycle_count = 1

    def print_display(self):
        for line in self.display:
            print(line)

    def process_cycle(self, instruction):
        if instruction == "noop":
            self.update_display_line(self.line_count)
            self.update_cycle_count()
        else:
            split_command = instruction.split()
            self.update_display_line(self.line_count)
            self.update_cycle_count()
            self.register += int(split_command[1])
            self.update_display_line(self.line_count)
            self.update_cycle_count()


# The actual executable portion
comm_unit = Processor()

with open("Data Files/Day 10 Data.txt", "r") as input:
    for line in input:
        comm_unit.process_cycle(line.strip("\n"))
    comm_unit.print_display()