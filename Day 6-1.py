# Advent of Code 2022 - Day 6 (Part 1)
# Scanning for a signal

class Scanner:
    def __init__(self):
        self.scan_slots = ["", "", "", ""]

    def is_duplicate(self, value_to_test):
        if self.scan_slots.count(value_to_test) > 1:
            return True
        else:
            return False

    def check_for_marker(self):
        valid_marker = True
        if self.scan_slots.count("") > 0:
            print("Incomplete marker!")
            valid_marker = False
        else:
            for time in range(4):
                # If there are any duplicates, then by definition the
                # code isn't a message
                if self.is_duplicate(self.scan_slots[time]):
                    valid_marker = False
        return valid_marker
    
    def check_for_message(self):
        valid_marker = True
        if self.scan_slots.count("") > 0:
            print("Incomplete marker!")
            valid_marker = False
        else:
            for time in range(14):
                if self.is_duplicate(self.scan_slots[time]):
                    valid_marker = False
        return valid_marker

    def add_value(self, value_to_add):
        # Shifts every value one 'slot' over, then adds the new one at the
        # end of the list.
        self.scan_slots[0] = self.scan_slots[1]
        self.scan_slots[1] = self.scan_slots[2]
        self.scan_slots[2] = self.scan_slots[3]
        self.scan_slots[3] = value_to_add
       

def find_first_marker(file_path):
    scanner_prop = Scanner()
    with open(file_path, "r") as input:
        test_string = input.read()
        for time in range(len(test_string)):
            scanner_prop.add_value(test_string[time])
            if scanner_prop.check_for_marker() == True:
                print("The first marker is after character " + str(time) + 1)
                break

find_first_marker("Data Files/Day 6 Data.txt")
