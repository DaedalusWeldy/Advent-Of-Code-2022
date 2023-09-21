# Advent of Code 2022 - Day 11 Part 2
# Confusing Primates, but big numbers?!

# Note that this problem is extremely open-ended, and what it's asking for
# is not well defined. I have done what I consider to be the simplest solution
# that still fulfills the requirements, but I have no way of interpereting
# what the puzzle makers want me to do to get at the answer.

class Monkey:
    def __init__(self, id_input = 0, inventory_input = [], operation_input = "",
                 logic_input = {}):
        self.id_number = id_input
        self.inventory = inventory_input
        self.inspect_operation = operation_input
        self.test_logic = logic_input
        self.monkey_counter = 0

    def add_inventory_item(self, value_to_add):
        self.inventory.append(value_to_add)

    def remove_inventory_item(self, index_to_remove):
        return self.inventory.pop(index_to_remove)
    
    def print_monkey(self):
        print("Monkey {}".format(self.id_number))
        print("Items are {}".format(self.inventory))
        print("The operation of this monkey is {}".format(self.inspect_operation))
        print("The test dividend of this monkey is {}".format(self.test_logic["divisible_by"]))
        print("->If that test is true, then send to monkey {}".format(self.test_logic["if_true"]))
        print("->If that test is false, then send to monkey {}".format(self.test_logic["if_false"]))

    def print_short_monkey(self):
        print("Monkey {}: {}".format(self.id_number, self.inventory))




# Scans the input file, creates each individual monkey and adds it to
# a list. Returns the list of created monkeys.
def parse_monkey_data(input_file):
    list_of_monkeys = []
    current_monkey = {}
    for line in input:
        stripped_line = line.strip("\n")
        # if line starts with "Monkey", trim the line and quantify the
        # ID of the current_monkey
        if stripped_line.startswith("Monkey"):
            line_segments = stripped_line.split()
            line_segments[1] = line_segments[1].strip(":")
            current_monkey["id"] = int(line_segments[1])
        # If line starts with " Starting Items:", trim the line, get the
        # list of item values and convert that list to intergers. Finally,
        # add that list to the current_monkey.
        elif stripped_line.startswith("  Starting items:"):
            trimmed_line = stripped_line[18:]
            trimmed_line = trimmed_line.strip(" ")
            item_list = []
            for item in trimmed_line.split(","):
                item_list.append(int(item))
            current_monkey["items"] = item_list
        # If line starts with " Operation:", then trim the line and add
        # the result to current_monkey as a string. The Monkey object we
        # turn this into will decode the string into something usable 
        elif stripped_line.startswith("  Operation:"):
            trimmed_line = stripped_line[19:]
            current_monkey["operation"] = trimmed_line
        # If line starts with " Test:" then trim the line. We make a new dict
        # named "test" and add trimmed_line as the "rule" value in it.
        elif stripped_line.startswith("  Test:"):
            trimmed_line = int(stripped_line[21:])
            current_monkey["test"] = {"divisible_by":trimmed_line}
        # If the line starts with "    If true:", then trim the line and get the
        # Id of the monkey it will throw to on "True". Assign that value to 
        # current_monkey["test"]["True"]
        # Note that the opposite will apply to "    If false:"
        elif stripped_line.startswith("    If true:"):
            trimmed_line  = stripped_line[29:]
            current_monkey["test"]["if_true"] = int(trimmed_line)
        elif stripped_line.startswith("    If false:"):
            trimmed_line  = stripped_line[30:]
            current_monkey["test"]["if_false"] = int(trimmed_line)
        # If the string is blank "", then we've reached the end of a monkey. pass
        # all of the current_monkey values to a new Monkey object and reset 
        # current_monkey for use in the next set.
        # Note that the dataset MUST have an empty line at the end for this to parse properly
        elif stripped_line == "":
            monkey_to_transfer = Monkey(current_monkey["id"], current_monkey["items"], 
                                        current_monkey["operation"], current_monkey["test"])
            list_of_monkeys.append(monkey_to_transfer)
            current_monkey = {}
        else:
            print("ERROR: Command was not recognized!")
    # At the end of the loop, return the list_of_monkeys
    return list_of_monkeys

def inspect_item(monkey_input, index_to_inspect):
    divided_instruction = monkey_input.inspect_operation.split()
    old_value = monkey_input.inventory[index_to_inspect]
    modifier_value = 0
    new_value = 0
    # create the old_value and the value it will be modified by
    if divided_instruction[2] == "old":
        modifier_value = old_value
    else:
        modifier_value = int(divided_instruction[2])
    # Determine what operator is being done, then perform the appropriate math
    if divided_instruction[1] == "+":
        new_value = old_value + modifier_value
    elif divided_instruction[1] == "-":
        new_value = old_value - modifier_value
    elif divided_instruction[1] == "*":
        new_value = old_value * modifier_value
    elif divided_instruction[1] == "/":
        new_value = old_value / modifier_value

    # I fully admit I had to ask for help with this line
    new_value = new_value % 9699690

    test_results = divmod(new_value, monkey_input.test_logic["divisible_by"])
    if new_value == 0 or test_results[1] == 0:
        monkey_input.remove_inventory_item(index_to_inspect)
        monkey_list[monkey_input.test_logic["if_true"]].add_inventory_item(new_value)
    else:
        monkey_input.remove_inventory_item(index_to_inspect)
        monkey_list[monkey_input.test_logic["if_false"]].add_inventory_item(new_value)
    
    # Add 1 to the value of monkey_counter
    monkey_input.monkey_counter += 1

# Main execution programming:
with open("Data Files/Day 11 Data.txt","r") as input:
    monkey_list = parse_monkey_data(input)
    for index in range(10000):
        for current_monkey in monkey_list:
            while len(current_monkey.inventory) > 0:
                inspect_item(current_monkey, 0)
    for current_monkey in monkey_list:
        print("Monkey {} passed {} times".format(current_monkey.id_number, 
                                                 current_monkey.monkey_counter))
