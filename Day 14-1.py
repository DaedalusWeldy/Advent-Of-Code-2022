# Advent of Code 2022 - Day 13 Part 1
# Falling Sands

import copy

# because we're not dealing with clean, low numbers, mapArray can't
# be a 2D array. Instead, we're using an array of dictionaries. The
# array is your Y coordinate, while the X coordinate acts as the key 
# for the dictionary in that row. the value of that key will be either
# air(.), rock (#), or sand (O).  
class TerrainMap:
    def __init__(self):
        self.map_array = []
        for index in range(175):
            row_dict = {}
            column_number = 450
            for index in range(125):
                row_dict[str(column_number)] = '.'
                column_number += 1
            self.map_array.append(row_dict)

    def print_map(self):
        with open("Output Files/Day 14 Output.txt", "w") as output:
            # Create the llist that will help label the top of the map
            x_label_list = []
            key_values = self.map_array[0].keys()
            for index in range(3):
                label_line = ""
                for entry in key_values:
                    label_line = label_line + entry[index]
                x_label_list.append(label_line)
            # Print x_label_list which will create the label at the top of the map
            for line in x_label_list:
                output.write(line + "\n")
            for row in self.map_array:
                row_string = ""
                for entry in row:
                    row_string = row_string + "" + (row[entry])
                output.write(row_string + "\n")

    def change_cell(self, pos_x, pos_y, new_value):
        # Have to call in y, x order due to array structure
        # Also have to offset the Y value by 1, due to arrays starting at 0
        self.map_array[int(pos_y) - 1][str(pos_x)] = new_value
        # TEST
        # print("position {}, {} has been changed to #.".format(pos_x, pos_y))

    def get_cell(self, pos_x, pos_y):
        return self.map_array[int(pos_y) - 1][str(pos_x)]

    # Find the direction of a new point in relation to another old point
    # inputs should be lists in [X, Y] format
    def find_point_direction(self, old_coords, new_coords):
        direction = ""
        if old_coords[0] > new_coords[0]:
            direction = "east"
        elif old_coords[0] < new_coords[0]:
            direction = "west"
        elif old_coords[1] > new_coords[1]:
            direction = "south"
        elif old_coords[1] < new_coords[1]:
            direction = "north"
        return direction

    # Take a list of points and map the rock formations that they depict.
    def fill_rock_pattern(self, rock_instruction_line):
        point_number = 1
        previous_coords = []
        stripped_line = rock_instruction_line.strip("\n")
        trimmed_list = stripped_line.split(" -> ")
        for point in trimmed_list:
            # Saves coordinates of point in [x, y] list format
            target_coords = point.split(",")
            target_coords[0] = int(target_coords[0])
            target_coords[1] = int(target_coords[1])
            if point_number == 1:
                self.change_cell(target_coords[0], target_coords[1], "#")
            else:
                if self.find_point_direction(previous_coords, target_coords) == "west":
                    difference = abs(previous_coords[0] - target_coords[0])
                    coord_progress = copy.copy(target_coords)
                    while difference > 0:
                        self.change_cell(coord_progress[0], coord_progress[1], "#")
                        difference -= 1
                        coord_progress[0] -= 1
                elif self.find_point_direction(previous_coords, target_coords) == "east":
                    difference = abs(previous_coords[0] - target_coords[0])
                    coord_progress = copy.copy(target_coords)
                    while difference > 0:
                        self.change_cell(coord_progress[0], coord_progress[1], "#")
                        difference -= 1
                        coord_progress[0] += 1
                elif self.find_point_direction(previous_coords, target_coords) == "south":
                    difference = abs(previous_coords[1] - target_coords[1])
                    coord_progress = copy.copy(target_coords)
                    while difference > 0:
                        self.change_cell(coord_progress[0], coord_progress[1], "#")
                        difference -= 1
                        coord_progress[1] += 1
                elif self.find_point_direction(previous_coords, target_coords) == "north":
                    difference = abs(previous_coords[1] - target_coords[1])
                    coord_progress = copy.copy(target_coords)
                    while difference > 0:
                        self.change_cell(coord_progress[0], coord_progress[1], "#")
                        difference -= 1
                        coord_progress[1] -= 1
            previous_coords = copy.copy(target_coords)
            point_number += 1

    def spawn_sand(self):
        # Specify the coordinates that sand will always drop at
        START_COORDS = [500, 0]
        current_coords = START_COORDS
        sand_is_falling = True
        falling_forever = False
        while current_coords[1] <= 165 and sand_is_falling:
            # First test directly below
            if self.get_cell(current_coords[0], current_coords[1] + 1) == ".":
                current_coords = [current_coords[0], current_coords[1] + 1]
            # Next, test diagonal left
            elif self.get_cell(current_coords[0] - 1, current_coords[1] + 1) == ".":
                current_coords = [current_coords[0] - 1, current_coords[1] + 1]
            # Next, test diagonal right
            elif self.get_cell(current_coords[0] + 1, current_coords[1] + 1) == ".":
                current_coords = [current_coords[0] + 1, current_coords[1] + 1]
            # Finally, if none of those are valid, put the grain of sand "O" 
            # on the current_coords.
            else:
                self.change_cell(current_coords[0], current_coords[1], "O")
                sand_is_falling = False
            
            if current_coords[1] == 165:
                falling_forever = True
        return falling_forever
        




test_map = TerrainMap()
fall_check = False
total_grains = 0
with open("Data Files/Day 14 Data.txt", "r") as input:
    for line in input:
        test_map.fill_rock_pattern(line)

while fall_check == False:
    if test_map.spawn_sand() == True:
        fall_check = True
    else:
        total_grains += 1
# TEST
test_map.print_map()
# Return 
print("The total number of grains before abyss is {}".format(total_grains))