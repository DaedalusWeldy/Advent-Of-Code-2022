# Advent of Code 2022 - Day 15 Part 1
# Sensors and beacons, and a specific y-level? 

import re

# Read and convert text list of coordinates into dicts
# Dicts will contain 'sensor' and 'beacon' keys, the values of which 
# will be in [X, Y] format.
def read_coords_list(file_input):
    coords_to_return = []
    for line in file_input:
        split_line = line.strip("\n")
        split_line = re.sub("[,:]", "", split_line)
        split_line = re.split("\s", split_line)
        split_line = [split_line[2], split_line[3], split_line[8], split_line[9]]
        read_sensor = [int(split_line[0][2:]), int(split_line[1][2:])]
        read_beacon = [int(split_line[2][2:]), int(split_line[3][2:])]
        sensor_beacon_pair = {"sensor": read_sensor, "beacon": read_beacon}
        coords_to_return.append(sensor_beacon_pair)
    
    return coords_to_return


# Merge two lists, skipping duplicate values
def combine_lists(original_list, list_to_join):
    for entry in list_to_join:
        if entry not in original_list:
            original_list.append(entry)
    original_list.sort()

# Find and return the "Manhattan Distance" of two points.
def find_manhattan_dist(start, end):
    # Manhattan distance is calulated by |x1 - x2| + |y1 - y2|
    result = abs(start[0] - end[0]) + (start[1] - end[1])
    return result

# Find how many points on the given row are 'marked' - that is, cannot 
# contain a beacon. Takes two tuples (the 'sensor' and the 'beacon' in (x,y
# format), returns a list of x-coordinates on the given row that are marked 
# by that sensor/beacon combo.
def generate_mark_list(target_y_level, sensor_coord, beacon_coord):
    list_to_return = []
    # find the manhattan distance between the sensor and the beacon. 
    distance = find_manhattan_dist(sensor_coord, beacon_coord)
    
    # find the 'y-dif', the difference between the target line and the 
    # y-cordinate of the sensor. We then use that to find the side length
    # and the total length of the target line. 
    y_dif = abs(sensor_coord[1] - target_y_level)
    side_length = distance - y_dif
    
    # We need to know how long the affected portion of the line is, as 
    # well as the length of one side. Keep in mind there will also be a 
    # central point between the two sides, so we add 1 to the total length. 
    line_length = 1 + (2 * side_length)
    start_point = sensor_coord[1] - side_length
    end_point = start_point + line_length
    for index in range(start_point, end_point + 1):
        if list_to_return.count(index) == 0:
            list_to_return.append(index)
    
    # sort the list and return it
    list_to_return = list_to_return.sort()
    return list_to_return


# TEST AREA
with open("Scratch Files/Day 15 Test.txt", "r") as test_input:
    coord_list = read_coords_list(test_input)
    print(coord_list)