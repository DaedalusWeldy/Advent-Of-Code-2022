# Advent of Code 2022 - Day 9 (Part 2)
# Rope Physics?!

class Rope:
    def __init__(self):
        self.knot_locations = []
        # Create nine 'tails' in the list, all starting at coords 0,0
        for index in range(10):
            self.knot_locations.append({"x": 0,"y": 0})
        self.tail_visit_list = ["0,0"]
    
    def tail_overlapping(self, lead_knot, head_to_test):
        is_overlapping = False
        if (lead_knot["x"] == head_to_test["x"] and 
            lead_knot["y"] == head_to_test["y"]):
            is_overlapping = True
        return is_overlapping
    
    # Calculates where one knot is in relation to a 'lead knot'.
    # For example: Head [2,3], Tail [1,2] OR Head [1,2], Tail [2,3]
    def compare_knot_locations(self, lead_knot, knot_to_test):
        location = ""
        # First, if the head and tail are in the same location, just list the 
        # location as "overlap" 
        if self.tail_overlapping(lead_knot, knot_to_test) == True:
            location = "overlap"
        # Second, if the head and tails are on the same x- or y-axis, then find
        # which direction the tail is in and set that as "location" (south, north,
        # west or east).
        elif lead_knot["x"] == knot_to_test["x"]:
            if lead_knot["y"] - knot_to_test["y"] > 0:
                location = "south"
            if lead_knot["y"] - knot_to_test["y"] < 0:
                location = "north"
        elif lead_knot["y"] == knot_to_test["y"]:
            if lead_knot["x"] - knot_to_test["x"] > 0:
                location = "west"
            if lead_knot["x"] - knot_to_test["x"] < 0:
                location = "east"
        # Finally, if the head and tail are not on either of the same axis, then
        # that means the tail is on one of the anti-cardinals (that is, diagonals).
        # find the North/South direction, then append the East/West to it.
        else:
            if lead_knot["y"] - knot_to_test["y"] > 0:
                location = "south"
            if lead_knot["y"] - knot_to_test["y"] < 0:
                location = "north"
            if lead_knot["x"] - knot_to_test["x"] > 0:
                location = location + "-west"
            if lead_knot["x"] - knot_to_test["x"] < 0:
                location = location + "-east"
        return location
    
    # TEST
    # HEAD [0, 1], TAIL [0,0]
    def is_outside_range(self, lead_knot, knot_to_test):
        result = True
        # using the absolute value, find out the distance from the lead to the test 
        # knot on the x- and y-axis. 
        x_distance = abs(lead_knot["x"] - knot_to_test["x"])
        y_distance = abs(lead_knot["y"] - knot_to_test["y"])
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
        tail_coords = "{},{}".format(self.knot_locations[9]["x"], self.knot_locations[9]["y"])
        if (self.tail_visit_list.count(tail_coords) < 1):
            self.tail_visit_list.append(tail_coords)
    
    def move_tails(self):
        for index in range(len(self.knot_locations)):
            if index == 0:
                pass
            else:
                current_knot = self.knot_locations[index]
                previous_knot = self.knot_locations[index - 1]
                tail_direction = self.compare_knot_locations(previous_knot,current_knot)
                if self.is_outside_range(previous_knot,current_knot) == True:
                    if tail_direction == "south":
                        self.knot_locations[index]["y"] += 1
                    elif tail_direction == "north":
                        self.knot_locations[index]["y"] -= 1
                    elif tail_direction == "west":
                        self.knot_locations[index]["x"] += 1
                    elif tail_direction == "east":
                        self.knot_locations[index]["x"] -= 1
                    elif tail_direction == "south-west":
                        self.knot_locations[index]["x"] += 1
                        self.knot_locations[index]["y"] += 1
                    elif tail_direction == "south-east":
                        self.knot_locations[index]["x"] -= 1
                        self.knot_locations[index]["y"] += 1
                    elif tail_direction == "north-west":
                        self.knot_locations[index]["x"] += 1
                        self.knot_locations[index]["y"] -= 1
                    elif tail_direction == "north-east":
                        self.knot_locations[index]["x"] -= 1
                        self.knot_locations[index]["y"] -= 1
            # The problem for this part only wants the coords of the last knot -
            # the tail. Thus, we only update the tail_visit_list on the last iteration
            if index == 9:
                self.update_tail_visit_list()
    
    # Move the head of the rope, then update the tail's location according
    # to the rules. Also, with every step we check the coordinates of the tail
    # and, if those coordinates are not already in the 'tail_visit_list', add it.
    def move_head(self, direction, steps):
        for index in range(steps):
            if direction == "U":
                self.knot_locations[0]["y"] += 1
            elif direction == "D":
                self.knot_locations[0]["y"] -= 1
            elif direction == "R":
                self.knot_locations[0]["x"] += 1
            elif direction == "L":
                self.knot_locations[0]["x"] -= 1
            # Update the tail position according to the rules outlined on the site
            self.move_tails()

elf_rope = Rope()

with open("Data Files/Day 9 Data.txt","r") as input:
    for line in input:
        filtered_line = line.strip("\n")
        command = filtered_line.split()
        # TEST
        print("Command is {}".format(command))
        elf_rope.move_head(command[0], int(command[1]))
        print(elf_rope.knot_locations)
    print("The total number of spaces the tail touched is {}".format(len(elf_rope.tail_visit_list)))