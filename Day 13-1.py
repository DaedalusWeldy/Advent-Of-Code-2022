# Advent of Code 2022 - Day 13 Part 1
# Comparing signals

# Using json to read the values from the data file
import json
import copy

class Signal:
    def __init__(self, left_signal, right_signal):
        self.left_signal = left_signal
        self.right_signal = right_signal

    def test_pair(self, left_input, right_input):
        # Making copies of the input lists, so that we don't affect the originals.
        copy_left = copy.copy(left_input)
        copy_right = copy.copy(right_input)
        while (len(copy_left) > 0 and len(copy_right) > 0):
            current_left = copy_left.pop(0)
            current_right = copy_right.pop(0)
            # If both inputs are intergers, simply test for the required values and 
            # return the result.
            if type(current_left) == int and type(current_right) == int:
                if current_left < current_right:
                    return "pass"
                elif current_left > current_right:
                    return "fail"
            elif type(current_left) == list and type(current_right) == list:
                results = self.test_pair(current_left, current_right)
                if results != "match":
                    return results
            elif ((type(current_left) == int and type(current_right) == list) or 
                (type(current_left) == list and type(current_right) == int)):
                left_list = []
                right_list = []
                # Assign left and right lists, appending or passing through
                # as necessary
                if type(current_left) == int:
                    left_list.append(current_left)
                elif type(current_left) == list:
                    left_list = current_left
                if type(current_right) == int:
                    right_list.append(current_right)
                elif type(current_right) == list:
                    right_list = current_right
                results = self.test_pair(left_list, right_list)
                if results != "match":
                    return results
        if len(left_input) < len(right_input):
            return "pass"
        elif len(left_input) > len(right_input):
            return "fail"
        else:
            return "match"

# TEST
# test_signal = Signal([1,1,3,1,1],[1,1,5,1,1])
# print(test_signal.test_pair(test_signal.left_signal, test_signal.right_signal))


def make_signal_list(file_input):
    list_of_signals = []
    current_signal_left = ""
    current_signal_right = ""
    current_line = "left"
    current_line_num = 0
    for entry in file_input:
        stripped_line = entry.strip("\n")
        if current_line == "left":
            current_signal_left = json.loads(stripped_line)
            current_line = "right"
        elif current_line == "right":
            current_signal_right = json.loads(stripped_line)
            current_line = "clear"
        elif current_line == "clear":
            list_of_signals.append(Signal(current_signal_left, current_signal_right))
            current_signal_left = ""
            current_signal_right = ""
            current_line = "left"
        current_line_num += 1
    # Append the final signal of the data file to the list
    list_of_signals.append(Signal(current_signal_left, current_signal_right))
    return list_of_signals


elf_signals = make_signal_list(open("Data Files/Day 13 Data.txt", "r"))
valid_entries = []
total_of_indicies = 0
entry_number = 1
for entry in elf_signals:
    # TEST
    print("Signal #{}'s value is {}".format(entry_number, entry.test_pair(entry.left_signal, entry.right_signal)))
    if entry.test_pair(entry.left_signal, entry.right_signal) == "pass":
        valid_entries.append(entry_number)
    entry_number += 1
for number in valid_entries:
    total_of_indicies += number
print("The total of the valid indicies is " + str(total_of_indicies))
