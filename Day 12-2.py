# Advent of Code 2022 - Day 12 Part 2
# Charting a path to the top... from any height 'a' space

# Didn't know BFS Search was a thing before this. That said, the implementation
# herein is my own implementation of the concept

class HeightMap:
    def __init__(self):
        self.map_array = []
        self.start_point = {"x":0, "y":0}
        self.end_point = {"x":0, "y":0}

    # Read the data from the input file. When creating each cell, we make it a
    # dict with two values: "height", measured by a lowercase letter, and 
    # "was_traversed", a boolean that registers whether or not a space has been 
    # visited before (at creation, all "was_traversed" will be false) 
    def create_map(self, file_to_read):
        current_line = 0
        with open(file_to_read, "r") as input:
            for line in input:
                segmented_line = []
                for index in range(len(line.strip("\n"))):
                    map_cell = {}
                    map_cell["height"] = line[index]
                    map_cell["was_traversed"] = False
                    segmented_line.append(map_cell)
                self.map_array.append(segmented_line)
                current_line += 1
        self.find_end_position()

    # A basic method to print the map
    def print_map(self):
        for line in self.map_array:
            joined_list = ""
            for item in line:
                joined_list = joined_list + item["height"]
            print(joined_list)

    # A method to convert the height of a given space into an int, to better
    # work with it in comparisons.
    def translate_height(self, height_to_test):
        translated_height = 0
        HEIGHT_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                       "k", "l", "m", "n", "o", "p", "q", "r", "s", "t" , 
                       "u", "v", "w", "x", "y", "z"]
        if height_to_test == "E":
            translated_height = 25
        elif height_to_test == "S":
            translated_height = 0
        else:
            translated_height = HEIGHT_LIST.index(height_to_test)
        return translated_height

    # Locate the position marked with an "S" and set it as the start point. 
    # Also mark the spot as visited (set "was_traversed" to True)
    def find_start_position(self):
        found_start = False
        coords = {"x":0, "y":0}
        # due to the way arrays are called, calls are done [y, x] instead
        # of [x, y]
        while found_start == False:
            if self.map_array[coords["y"]][coords["x"]]["height"] == "S":
                found_start = True
            else:
                if coords["x"] == (len(self.map_array[coords["y"]]) - 1):
                    coords["x"] = 0
                    coords["y"] += 1
                elif coords["x"] < (len(self.map_array[coords["y"]]) - 1):
                    coords["x"] += 1
        self.start_point = coords
        # Mark the starting point as having been traversed
        self.map_array[coords["y"]][coords["x"]]["was_traversed"] = True

    # Mark the position of the space with "E" as the end point
    def find_end_position(self):
        found_end = False
        coords = {"x":0, "y":0}
        # due to the way arrays are called, calls are done [y, x] instead
        # of [x, y]
        while found_end == False:
            if self.map_array[coords["y"]][coords["x"]]["height"] == "E":
                found_end = True
            else:
                if coords["x"] == (len(self.map_array[coords["y"]]) - 1):
                    coords["x"] = 0
                    coords["y"] += 1
                elif coords["x"] < (len(self.map_array[coords["y"]]) - 1):
                    coords["x"] += 1
        self.end_point = coords

    # change the "was_visited" value of a given spot on the map to "True" 
    def mark_as_visited(self, target_coords):
        self.map_array[target_coords["y"]][target_coords["x"]]["was_traversed"] = True

    # Resets the "was_traversed" of every space to "False" 
    def clear_all_spaces(self):
        for row in self.map_array:
            for cell in row:
                cell["was_traversed"] = False

    # Check if the given coordinates are within the grid
    def is_within_grid(self, coords):
        x_is_valid = False
        y_is_valid = False
        if 0 <= coords["y"] <= (len(self.map_array) - 1):
            y_is_valid = True
        if 0 <= coords["x"] <= (len(self.map_array[0]) - 1):
            x_is_valid = True
        # If both x and y are valid, then the coordinates are within
        # the grid, and this method should return True. Otherwise, return 
        # false.
        if x_is_valid == True and y_is_valid == True:
            return True
        else:
            return False

    # Check if an target square is, at most, one height higher than the current coordinates.    
    def is_proper_height(self, current_coords, target_coords):
        current_height = self.translate_height(self.map_array[current_coords["y"]][current_coords["x"]]["height"])
        target_height = self.translate_height(self.map_array[target_coords["y"]][target_coords["x"]]["height"])
        if (target_height <= current_height + 1):
            return True
        else:
            return False

    #check if the coordinates specified have been visited yet.    
    def is_not_visited(self, coords):
        if self.map_array[coords["y"]][coords["x"]]["was_traversed"] == False:
            return True
        else:
            return False
    
    def find_valid_directions(self, coords):
        north_coords = {"x": coords["x"], "y": coords["y"] - 1}
        south_coords = {"x": coords["x"], "y": coords["y"] + 1}
        east_coords = {"x": coords["x"] + 1, "y": coords["y"]}
        west_coords = {"x": coords["x"] - 1, "y": coords["y"]}
        # Test for three separate things:
        # -- if the current current_coords are a part of the grid, 
        # -- If the target height is more than one step up from the current height. 
        # -- If the space in question has a "has_traversed" value of True
        # If any one of those three are true, then set the direction being tested as
        # a simple string: "Not Valid"
        if (self.is_within_grid(north_coords) == False or 
            self.is_proper_height(coords, north_coords) == False or
            self.is_not_visited(north_coords) == False):
            north_coords = "Not Valid"
        # Same test, but for south direction
        if (self.is_within_grid(south_coords) == False or 
            self.is_proper_height(coords, south_coords) == False or
            self.is_not_visited(south_coords) == False):
            south_coords = "Not Valid"
         # Same test, but for east direction
        if (self.is_within_grid(east_coords) == False or 
            self.is_proper_height(coords, east_coords) == False or
            self.is_not_visited(east_coords) == False):
            east_coords = "Not Valid"
        # Same test, but for west direction
        if (self.is_within_grid(west_coords) == False or 
            self.is_proper_height(coords, west_coords) == False or
            self.is_not_visited(west_coords) == False):
            west_coords = "Not Valid"
        # gather all of the results in a single list for easy export
        coords_result_list = [north_coords, south_coords, east_coords, west_coords]
        return coords_result_list

        
    def find_path_to_end(self, start_point):
        found_exit = False
        self.mark_as_visited(start_point)
        to_visit_queue = [start_point]
        to_visit_queue[0]["steps"] = 0
        shortest_coords = {}
        while len(to_visit_queue) > 0 and found_exit == False:
            current_coords = to_visit_queue.pop(0)
            if (current_coords["x"] == self.end_point["x"] and
                current_coords["y"] == self.end_point["y"]):
                shortest_coords = current_coords
                found_exit = True
                break
            else:
                adjacent_coords = self.find_valid_directions(current_coords)
                for value in adjacent_coords:
                    if value != "Not Valid" and value not in to_visit_queue:
                        value["steps"] = current_coords["steps"] + 1
                        to_visit_queue.append(value)
                        self.mark_as_visited(value)
        if found_exit == True:
            return shortest_coords
        else:
            return "ERROR"
            
    def find_closest_low_point(self):
        point_list = []
        for row_num in range(len(self.map_array)):
            for column_num in range(len(self.map_array[0])):
                if self.translate_height(self.map_array[row_num][column_num]["height"]) == 0:
                    test_coords = {"x":column_num, "y": row_num}
                    path_result = self.find_path_to_end(test_coords)
                    if path_result != "ERROR":
                        print("Found a viable path: {}".format(path_result))
                        point_list.append(path_result)
                    self.clear_all_spaces()
        # Sort the list of points that were successful by "steps" and return the result
        # With the lowest value
        point_list.sort(key=lambda x: x["steps"])
        print("The shortest distance is {} steps.".format(point_list[0]))


jungle = HeightMap()
jungle.create_map("Data Files/Day 12 Data.txt")
# jungle.print_map()
jungle.find_closest_low_point()