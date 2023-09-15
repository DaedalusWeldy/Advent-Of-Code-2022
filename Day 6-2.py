# Advent of Code 2022 - Day 6 (Part 2)
# Scanning for a longer signal

class Scanner:
    def __init__(self):
        self.scan_slots = []

    def is_duplicate(self, value_to_test):
        if self.scan_slots.count(value_to_test) > 1:
            return True
        else:
            return False
    
    def check_for_message(self):
        valid_marker = True
        if len(self.scan_slots) < 14:
            print("Incomplete marker!")
            valid_marker = False
        else:
            for time in range(14):
                # If there are any duplicates, then by definition the
                # code isn't a message
                if self.is_duplicate(self.scan_slots[time]):
                    valid_marker = False
        return valid_marker

    def add_value(self, value_to_add):
        if len(self.scan_slots) < 14:
            self.scan_slots.append(value_to_add)
        else:
            self.scan_slots.append(value_to_add)
            self.scan_slots.pop(0)
       

def find_first_marker(file_path):
    scanner_prop = Scanner()
    with open(file_path, "r") as input:
        test_string = input.read()
        for time in range(len(test_string)):
            # Add the current character to the scanner
            scanner_prop.add_value(test_string[time])
            if scanner_prop.check_for_marker() == True:
                print("The first marker is after character " + str(time) + 1)
                break

def find_first_message(file_path):
    scanner_prop = Scanner()
    with open(file_path, "r") as input:
        test_string = input.read()
        for time in range(len(test_string)):
            # Add the current character to the scanner
            scanner_prop.add_value(test_string[time])
            if scanner_prop.check_for_message() == True:
                print("The first marker is after character " + str(time + 1))
                break

find_first_message("Data Files/Day 6 Data.txt")
