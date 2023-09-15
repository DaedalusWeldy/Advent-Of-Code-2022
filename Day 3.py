# Day 3 of Advent of Code 2022
# Rucksack Priority
from string import ascii_lowercase, ascii_uppercase

def containsItem(input_string, char_to_find):
    if input_string.count(char_to_find) != 0:
        return True
    else:
        return False

def findCommonItem(input_string):
    # Divide the rucksack string into two separate strings 
    # of equal length.
    compartment_size = int(len(input_string) / 2)
    first_compartment = input_string[:compartment_size]
    second_compartment = input_string[compartment_size:]
    # Find the common item (character) between the two 
    # compartments using 'containsItem'.
    found_common_item = False
    common_item = ""
    # search the compartments for all lowercase letters
    for entry in ascii_lowercase:
        if containsItem(first_compartment, entry) and containsItem(second_compartment, entry):
            common_item = entry
            found_common_item = True
            break
    # If no lowercase letter was found, do the same thing 
    # for uppercase letters 
    if found_common_item == False:
        for entry in ascii_uppercase:
            if containsItem(first_compartment, entry) and containsItem(second_compartment, entry):
                common_item = entry
                found_common_item = True
                break
    # either print an error or return the character common
    # to both compartments
    if found_common_item == False:
        print("ERROR: no match found.")
    else:
        return common_item

# Part 2 Exercise: find the common item type (character) 
# between three packs. Largely copied from findCommonItem
# as defined above
def findCommonBadgeType(pack_one_input, pack_two_input, pack_three_input):
    found_common_item = False
    common_item = ""
    # search the compartments for all lowercase letters
    for entry in ascii_lowercase:
        if containsItem(pack_one_input, entry) and containsItem(pack_two_input, entry) and containsItem(pack_three_input, entry):
            common_item = entry
            found_common_item = True
            break
    # If no lowercase letter was found, do the same thing 
    # for uppercase letters 
    if found_common_item == False:
        for entry in ascii_uppercase:
            if containsItem(pack_one_input, entry) and containsItem(pack_two_input, entry) and containsItem(pack_three_input, entry):
                common_item = entry
                found_common_item = True
                break
    # either print an error or return the character common
    # to both compartments
    if found_common_item == False:
        print("ERROR: no match found.")
    else:
        # TEST
        print(common_item)
        return common_item

    
def calculatePriority(char_input):
    # Add 1 to each result from ascii_lowercase
    lowercase_weight = 1 
    # Add 26 to each result from ascii_uppercase
    uppercase_weight = 27
    if char_input in ascii_lowercase:
        return ascii_lowercase.index(char_input) + lowercase_weight
    elif char_input in ascii_uppercase:
        return ascii_uppercase.index(char_input) + uppercase_weight
    else:
        print("ERROR: character not an uppercase or lowercase letter")


# Main execution code below

with open("Data Files/Day 3 Data.txt", "r") as file_input:
    priority_total = 0
    elf_count = 0
    current_trio = ["X", "Y", "Z"]
    for entry in file_input:
        if elf_count <= 2:
            current_trio[elf_count] = entry
            # TEST
            print("Elf number " + str(elf_count) + ": " + current_trio[elf_count])
            elf_count = elf_count + 1
        
        if elf_count == 3:
            common_item = findCommonBadgeType(current_trio[0], current_trio[1], current_trio[2])
            priority_total += calculatePriority(common_item)
            elf_count = 0
            current_trio = ["X", "Y", "Z"]
    print("Total priority is " + str(priority_total))
