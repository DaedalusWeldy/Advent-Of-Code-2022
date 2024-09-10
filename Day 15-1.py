# Advent of Code 2022 - Day 15 Part 1
# Sensors and beacons, and a specific y-level? 

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
    for index in range(start_point, end_point):
        