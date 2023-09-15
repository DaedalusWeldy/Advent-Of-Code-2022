# Advent of Code 2022 - Day 8
# Building Treehouses, Finding Cover

class Forest:
    def __init__(self):
        self.forest_plot = []
        self.current_height = 0

    # Adds a row to the bottom of the 'forest_plot' grid
    # i.e. it becomes the last row
    def add_row(self, row_input):
        separated_row = []
        for item_index in range(len(row_input)):
            separated_row.append(int(row_input[item_index]))
        self.forest_plot.append(separated_row)
        self.current_height += 1

    def tree_is_at_edge(self, row_input, column_input):
        visible = False
        if (row_input == 0 or row_input == len(self.forest_plot[0]) or
            column_input == 0 or column_input == self.current_height - 1):
            visible = True
        return visible
        

    # Takes a pair of (x, y) coordintates, then scans the row and column
    # that it's in. If, in any of the four directions, there is no tree taller
    # then the specified one, the tree is visible, and the method returns 'True'.
    # Note that we must go in reverse order for calls to the 'forest_plot': [Y], 
    # then [X]
    def tree_is_visible(self, row_input, column_input):
        visible = False
        # First, the easy stuff: if X is the start or end of it's row, 
        # or if Y is in the top or bottom of it's column, then it's visible 
        # and thus True
        if self.tree_is_at_edge(row_input, column_input) == True:
            visible = True
        else:
            visible_west = True
            visible_east = True
            visible_north = True
            visible_south = True
            # Make a check to scan all four cardinal directions, and determine
            # if the tree is visible from each of them.
            tree_height = self.forest_plot[row_input][column_input]
            # Testing West visibility
            for item_x in range(column_input):
                if self.forest_plot[row_input][item_x] >= tree_height:
                    visible_west = False
                    break
            # Testing East visibility
            for item_x in range(column_input + 1, len(self.forest_plot[row_input])):
                if self.forest_plot[row_input][item_x] >= tree_height:
                    visible_east = False
                    break
            # Testing North visibility
            for item_y in range(row_input):
                if self.forest_plot[item_y][column_input] >= tree_height:
                    visible_north = False
                    break
            # Testing South visibility
            for item_y in range(row_input + 1, self.current_height):
                if self.forest_plot[item_y][column_input] >= tree_height:
                    visible_south = False
                    break
            # If any of the four directions are still True after testing, turn
            # 'visible' to True. 
            if (visible_north == True or visible_south == True or 
                visible_east == True or visible_west == True):
                visible = True
        return visible
    
    def get_tree_scenic_value(self, row_input, column_input):
        west_value = 0
        east_value = 0
        north_value = 0
        south_value = 0
        tree_height = self.forest_plot[row_input][column_input]
        # Testing all trees West of target
        if column_input != 0:
            current_column = column_input - 1
            is_blocking = False
            while is_blocking == False and current_column >= 0:
                if self.forest_plot[row_input][current_column] < tree_height:
                    west_value += 1
                    current_column -= 1
                else:
                    west_value += 1
                    is_blocking = True
        # Testing East visibility
        if column_input != len(self.forest_plot[row_input]):
            current_column = column_input + 1
            is_blocking = False
            while is_blocking == False and current_column <= len(self.forest_plot[row_input]) - 1:
                if self.forest_plot[row_input][current_column] < tree_height:
                    east_value += 1
                    current_column += 1
                else:
                    east_value += 1
                    is_blocking = True
        # Testing North visibility
        if row_input != 0:
            current_row = row_input - 1
            is_blocking = False
            while is_blocking == False and current_row >= 0:
                if self.forest_plot[current_row][column_input] < tree_height:
                    north_value += 1
                    current_row -= 1
                else:
                    north_value += 1
                    is_blocking = True
        # Testing South visibility
        if row_input != len(self.forest_plot):
            current_row = row_input + 1
            is_blocking = False
            while is_blocking == False and current_row <= len(self.forest_plot) - 1:
                if self.forest_plot[current_row][column_input] < tree_height:
                    south_value += 1
                    current_row += 1
                else:
                    south_value += 1
                    is_blocking = True
        # Get the scenic value of the selected tile by multiplying all four values
        scenic_value = (west_value * east_value * north_value * south_value)
        return scenic_value

elf_forest = Forest()

with open("Data Files/Day 8 Data.txt", "r") as input:
    # Import all lines from data into the Forest object
    for line in input:
        elf_forest.add_row(line.strip("\n"))
    # Iterate though each item in each row, feeding it's coordinates into the
    # 'tree_is_visible' method. Every time it gets a 'True' value, iterate 
    # 'total_visible_trees' by 1
    total_visible_trees = 0
    for row in range(len(elf_forest.forest_plot)):
        for column in range(len(elf_forest.forest_plot[row])):
            if elf_forest.tree_is_visible(row, column):
                total_visible_trees += 1
    print ("The total number of visible trees is " + str(total_visible_trees))

    best_scenic_value = {"cell": "1,1", "scenic_value":0}        
    for row in range(len(elf_forest.forest_plot)):
        for column in range(len(elf_forest.forest_plot[row])):
            if elf_forest.get_tree_scenic_value(row, column) > best_scenic_value["scenic_value"]:
                best_scenic_value["cell"] = "Y{}, X{}".format(row + 1, column + 1)
                best_scenic_value["scenic_value"] = elf_forest.get_tree_scenic_value(row, column)
    
    print("The best scenic value is {} with a score of {}".format(best_scenic_value["cell"], 
                                                                  best_scenic_value["scenic_value"]))
