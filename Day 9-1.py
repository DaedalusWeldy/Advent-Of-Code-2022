# Advent of Code 2022 - Day 9 (Part 1)
# Rope Physics?!

class Rope:
    def __init__(self):
        self.head_location = [0,0]
        self.tail_location = [0,0]
        self.tail_visit_list = ["0,0"]
    
    def tail_overlapping(self):
        is_overlapping = False
        if (self.head_location[0] == self.tail_location[0] and 
            self.head_location[1] == self.tail_location[1]):
            is_overlapping = True
        return is_overlapping
    
    # Calculates where the tail is in relation to the rope's head.
    # For example: Head [2,3], Tail [1,2] OR Head [1,2], Tail [2,3]
    def compare_to_head_location(self):
        location = ""
        # First, if the head and tail are in the same location, just list the 
        # location as "overlap" 
        if self.tail_overlapping() == True:
            location = "overlap"
        # Second, if the head and tails are on the same x- or y-axis, then find
        # which direction the tail is in and set that as "location" (south, north,
        # west or east).
        elif self.head_location[0] == self.tail_location[0]:
            if self.head_location[1] - self.tail_location[1] > 0:
                location = "south"
            if self.head_location[1] - self.tail_location[1] < 0:
                location = "north"
        elif self.head_location[1] == self.tail_location[1]:
            if self.head_location[0] - self.tail_location[0] > 0:
                location = "west"
            if self.head_location[0] - self.tail_location[0] < 0:
                location = "east"
        # Finally, if the head and tail are not on either of the same axis, then
        # that means the tail is on one of the anti-cardinals (that is, diagonals).
        # find the North/South direction, then append the East/West to it.
        else:
            if self.head_location[1] - self.tail_location[1] > 0:
                location = "south"
            if self.head_location[1] - self.tail_location[1] < 0:
                location = "north"
            if self.head_location[0] - self.tail_location[0] > 0:
                location = location + "-west"
            if self.head_location[0] - self.tail_location[0] < 0:
                location = location + "-east"
        return location
    
    # TEST
    # HEAD [0, 1], TAIL [0,0]
    def is_outside_range(self):
        result = True
        # using the absolute value, find out the distance from the head to tail
        # on the x- and y-axis. 
        x_distance = abs(self.head_location[0] - self.tail_location[0])
        y_distance = abs(self.head_location[1] - self.tail_location[1])
        # If the head and tail overlap, then they are still in range. Set result 
        # to False.
        if x_distance == 0 and y_distance == 0:
            result = False
        # If either the x- or y- axis is equal to or less than 1, then the head is 
        # within range of the tail. Set result to "False"
        if x_distance <= 1 and y_distance <= 1:
                result = False
        return result
    
    # Update the tail_visit_list with the current location of the tail, provided 
    # the current coordinates are NOT already on the list.
    def update_tail_visit_list(self):
        tail_coords = "{},{}".format(self.tail_location[0], self.tail_location[1])
        if (self.tail_visit_list.count(tail_coords) < 1):
            self.tail_visit_list.append(tail_coords)
    
    def move_tail(self):
        tail_direction = self.compare_to_head_location()
        if self.is_outside_range() == True:
            if tail_direction == "south":
                self.tail_location[1] += 1
            elif tail_direction == "north":
                self.tail_location[1] -= 1
            elif tail_direction == "west":
                self.tail_location[0] += 1
            elif tail_direction == "east":
                self.tail_location[0] -= 1
            elif tail_direction == "south-west":
                self.tail_location[0] += 1
                self.tail_location[1] += 1
            elif tail_direction == "south-east":
                self.tail_location[0] -= 1
                self.tail_location[1] += 1
            elif tail_direction == "north-west":
                self.tail_location[0] += 1
                self.tail_location[1] -= 1
            elif tail_direction == "north-east":
                self.tail_location[0] -= 1
                self.tail_location[1] -= 1
        self.update_tail_visit_list()
    
    # Move the head of the rope, then update the tail's location according
    # to the rules. Also, with every step we check the coordinates of the tail
    # and, if those coordinates are not already in the 'tail_visit_list', add it.
    def move_head(self, direction, steps):
        for index in range(steps):
            if direction == "U":
                self.head_location[1] += 1
            elif direction == "D":
                self.head_location[1] -= 1
            elif direction == "R":
                self.head_location[0] += 1
            elif direction == "L":
                self.head_location[0] -= 1
            # Update the tail position according to the rules outlined on the site
            self.move_tail()

elf_rope = Rope()

with open("Data Files/Day 9 Data.txt","r") as input:
    for line in input:
        filtered_line = line.strip("\n")
        command = filtered_line.split()
        # TEST
        print("Command is {}".format(command))
        elf_rope.move_head(command[0], int(command[1]))
        # TEST
        print("Head is at X{}, Y{}".format(elf_rope.head_location[0], elf_rope.head_location[1]))
        print("Tail is at X{}, Y{}".format(elf_rope.tail_location[0], elf_rope.tail_location[1]))
    print("The total number of spaces the tail touched is {}".format(len(elf_rope.tail_visit_list)))