# Advent of Code 2022 - Day 5
# Sorting crates


class BoxStack:
    def __init__(self):
        self.stack_contents = []
        self.stack_height = 0
        
    def get_stack_height(self):
        return self.stack_height

    # Note: this method can add one or multiple boxes,depending on whether
    # it's provided a character or a list
    def add_boxes_to_top(self, boxes_to_add):
        self.stack_contents.extend(boxes_to_add)
        self.stack_height = len(self.stack_contents)

    def add_boxes_to_bottom(self, boxes_to_add):
        self.stack_contents.insert(0, boxes_to_add)
        self.stack_height = len(self.stack_contents)

    # PART 1 - Picks up boxes one at a time
    def remove_boxes_9000(self, number_of_boxes):
        removed_boxes_stack = []
        for time in range(number_of_boxes):
            removed_boxes_stack.append(self.stack_contents.pop())
        self.stack_height = len(self.stack_contents)
        # Removed boxes maintain FIFO (first in, first out) order,
        # in keeping with the requirelents of part 1 of the puzzle
        return removed_boxes_stack
    
    # PART 2 - Picks up multiple boxes at once
    def remove_boxes_9001(self, number_of_boxes):
        removed_boxes_stack = self.stack_contents[(number_of_boxes * -1):]
        del self.stack_contents[(number_of_boxes * -1):]
        self.stack_height = len(self.stack_contents)
        # Removed boxes maintain FIFO (first in, first out) order,
        # in keeping with the requirelents of part 2 of the puzzle
        return removed_boxes_stack
    
    def print_stack(self, stack_number):
        output_string = ""
        for entry in self.stack_contents:
            output_string = output_string + ("[" + entry + "] ")
        print("Stack #{0}: {1}".format(stack_number, output_string))

    def get_top_box(self):
        return self.stack_contents[-1]

class storageArea:
    def __init__(self):
        self.stack_list = []
        self.max_height = 0

    def add_empty_stack(self):
        stack_to_add = BoxStack()
        self.stack_list.append(stack_to_add)

    def add_existing_stack(self, stack_to_add):
        self.stack_list.append(stack_to_add)
    
    def find_max_height(self):
        self.maxHeight = 0
        for entry in self.stack_list:
            if entry.get_stack_height() > self.maxHeight:
                self.maxHeight = entry.get_stack_height()

    def load_starting_state(self, diagram_input):
        # create a number of empty stacks equal to the number of stacks in
        # the diagram.
        for time in range(len(diagram_input[0])):
            self.add_empty_stack()
        # Run through the each line of the 'diagram_input'
        for line in diagram_input:
            # iterates character by character, adding them to the appropriate
            # Stack object if the character isn't a blank space.
            for time in range(len(line)):
                if line[time] != ' ':
                    self.stack_list[time].add_boxes_to_top(line[time])
        self.find_max_height()

    def move_boxes(self, number_to_move, start_stack, ending_stack):
        crane_stack = self.stack_list[start_stack].remove_boxes_9001(number_to_move)
        self.stack_list[ending_stack].add_boxes_to_top(crane_stack)

    def process_manifest(self, file_path):
        with open(file_path, "r") as file_input:
            diagram = []
            move_number = 1
            for entry in file_input:
                # If the line contains crate data, separate it and add it to the 
                # diagram list.
                if entry.startswith("["):
                    filtered_line = entry[1:-1:4]
                    diagram.insert(0, filtered_line)
                # If the entry is the number label at the bottom of the crate stacks,
                # then the diagram is finished. Send the diagram to the 'loadStartingState'
                # method to create the initial setup of the stacks.
                elif entry.startswith(" 1"):
                    self.load_starting_state(diagram)
                    self.print_storage_area()
                # If the entry is a move command, strip out the extra string data, then
                # send the necessary intergers to the 'MoveBoxes' method of elf_stacks
                elif entry.startswith("move"):
                    print("Move #" + str(move_number))
                    segmented_string = entry.split(" ")
                    modified_entry = segmented_string[1::2]
                    # TEST
                    # print(modified_entry)
                    # Must modify every number by 1?
                    self.move_boxes(int(modified_entry[0]), int(modified_entry[1]) - 1,
                                     int(modified_entry[2]) - 1)
                    move_number += 1
                    self.print_storage_area()
                    print("*****")

    def print_storage_area(self):
        for entry in range(len(self.stack_list)):
            self.stack_list[entry].print_stack(entry + 1)

    def print_first_solution(self):
        solution = []
        for entry in self.stack_list:
            solution.append(entry.get_top_box())
        print(solution)

# Main program area

elf_storage = storageArea()

elf_storage.process_manifest("Data Files/Day 5 Data.txt")