# Day 1 of the "Advent of Code 2022" coding challenge
from pathlib import Path



# Iterates a list and finds the elf with the highest total calorie count
def whoHasHighest(list_input):
    highest_count_elf = {"calories": 0}
    for entry in list_input:
        if entry["calories"] > highest_count_elf["calories"]:
            highest_count_elf = entry
    print("The elf with the highest calorie count is Elf " + str(highest_count_elf["elf_id"])
            + " with " + str(highest_count_elf["calories"]))

def sortFunction(input):
    return input["calories"]

def whoHasTopThree(list_input):
    list_input.sort(reverse=True, key=sortFunction)
    top_three_total = list_input[0]["calories"] + list_input[1]["calories"] + list_input[2]["calories"]
    print("First place is Elf " + str(list_input[0]["elf_id"]) + " with " + str(list_input[0]["calories"]))
    print("First place is Elf " + str(list_input[1]["elf_id"]) + " with " + str(list_input[1]["calories"]))
    print("First place is Elf " + str(list_input[2]["elf_id"]) + " with " + str(list_input[2]["calories"]))
    print("The total calories of the top three is " + str(top_three_total))

# Each entry in the list of elves will be a dict with an elf_name ("Elf 1", 
# "Elf 2", etc.) and a calorie_count 
elf_roster = []

with open("Data Files/Day 1 Data.txt", "r") as file_input:
# Start with the first elf. Will be incremented upwards every time the program hits
# a blank spot on the list.
    current_elf_id = 1
    current_elf = {"elf_id": current_elf_id, "calories":0}
    for entry in file_input:
        if entry != "\n":
            current_elf["calories"] += int(entry)
        else:
            # TEST need values for all elves for debug
            print("Elf number " + str(current_elf["elf_id"]) + " has " + str(current_elf["calories"]))
            elf_roster.append(current_elf)
            current_elf_id += 1
            current_elf = current_elf = {"elf_id": current_elf_id, "calories":0}
        # We need one final call to calculate and add the final elf to the roster
    elf_roster.append(current_elf)

whoHasTopThree(elf_roster)
