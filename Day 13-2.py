# Advent of Code 2022 - Day 13 Part 1
# Comparing signals

# Using json to read the values from the data file
import json
import copy

def test_pair(left_input, right_input):
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
            results = test_pair(current_left, current_right)
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
            results = test_pair(left_list, right_list)
            if results != "match":
                return results
    if len(left_input) < len(right_input):
        return "pass"
    elif len(left_input) > len(right_input):
        return "fail"
    else:
        return "match"


# Our new signal list is just a list of all the signals in order
def make_signal_list(file_input):
    list_of_signals = []
    # Adding in the two 'divider packets' from part 2
    for entry in file_input:
        stripped_line = entry.strip("\n")
        if stripped_line != "":
            list_of_signals.append(json.loads(stripped_line))
    return list_of_signals


elf_signals = make_signal_list(open("Data Files/Day 13 Data.txt", "r"))
# We don't need to sort the signal list; instead, we just need to find how many
# of the entries in elf_signals pass the 'test_pair' method when compared to the
# divider packets. Note that, when doing this, we have to add one to two's index
# number and 2 to six's.
key_indicies = {"two":1, "six":2}
# Sort the elf_signals list to put all signals in the proper order
for entry in elf_signals:
    if test_pair(entry, [[2]]) == "pass":
        key_indicies["two"] += 1
    if test_pair(entry, [[6]]) == "pass":
        key_indicies["six"] += 1

decoder_key = key_indicies["two"] * key_indicies["six"]
print("The decoder key is {}".format(decoder_key))
