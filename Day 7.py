# Advent of Code 2022 - Day 7
# Maintaining a file system

class File:
    def __init__(self, name_input, size_input = 0):
        self.name = name_input
        self.size = size_input

    def get_name(self):
        return self.name
        
    def get_size(self):
        return self.size
    
    def test_size(self, test_value):
        if self.size <= test_value:
            return True
        else:
            return False


class Folder(File):
    def __init__(self, name_input, path_input = "/"):
        super().__init__(name_input)
        self.path = path_input
        self.contents = []

    def get_path(self):
        return self.path

    def calculate_size(self):
        total_size = 0
        for entry in self.contents:
            total_size += entry.get_size()
        self.size = total_size

    def add_file(self, file_name, file_size):
        file_to_add = File(file_name, file_size)
        self.contents.append(file_to_add)
        self.calculate_size()

    def add_folder(self, folder_name, folder_path):
        folder_to_add = Folder(folder_name, folder_path)
        self.contents.append(folder_to_add)

    def sort_contents(self):
        folder_list = []
        file_list = []
        for entry in self.contents:
            if isinstance(entry, Folder):
                folder_list.append(entry)
            else:
                file_list.append(entry)
            folder_list.sort(key=lambda x: x.get_name())
            file_list.sort(key=lambda x: x.get_name())
            self.contents = folder_list + file_list

    def print_folder(self, level = 0):
        print(("--" * level) + "DIR {}: TOTAL {}".format(self.get_name(), self.get_size()))
        self.sort_contents()
        for entry in self.contents:
            dashes = "--" * (level + 1)
            if isinstance(entry, Folder):
                entry.print_folder(level + 1)
            else:
                print(dashes + "{} {}".format(entry.get_size(), entry.get_name()))


class FileStructure:
    def __init__(self):
        self.drive = Folder("Root", "/")
        self.current_path = "/"

    def current_path_is_root(self):
        if self.current_path == "/":
            return True
        else:
            return False

    def target_folder(self, path_input):
        target_folder = self.drive
        if self.current_path_is_root() == False:
            # split the inputted path into an iterable list
            parsed_path = path_input.split("/")
            for level in parsed_path:
                # only continue if the current level of the path is NOT blank
                if level != "":
                    # iterate through the contents of the current target_folder,
                    # find the desired folder and replace target_folder with it.
                    # Then break the iteration loop once that's done.
                    for entry in target_folder.contents:
                        if entry.get_name() == level:
                            target_folder = entry
                            break
        return target_folder

    def change_path(self, target_path):
        # TEST
        print("CHANGE_PATH: target_path is " + str(target_path))
        # If the command target is '/', set current path to the root
        if target_path == "/":
            self.current_path = target_path
        # If the command target is '..', set current path to one folder
        # 'above' the current one
        elif target_path == "..":
            segmented_path = self.current_path.split("/")
            segmented_path.pop(-1)
            self.current_path = "/".join(segmented_path)
        # Finally, if the command target is a folder name, add it to 
        # the end of the current path
        else:
            segmented_path = []
            # If thecurrent_path is at the root ("/"), then make the segmented_path 
            # a single-entry list. Otherwise, split the current_path into a list of
            # individual, concurrent folders.
            if self.current_path_is_root():
                segmented_path = ["/"]
                segmented_path.append(target_path)
                self.current_path = "".join(segmented_path)
            else:
                segmented_path = self.current_path.split("/")
                segmented_path.append(target_path)
                self.current_path = "/".join(segmented_path)
        print("CHANGE_PATH: current_path is now " + str(self.current_path))

    def add_folder_at_location(self, folder_name):
        # 'Navigate' to the target are where we want to create the 
        # folder. 
        target_folder = self.target_folder(self.current_path)
        # Add a new dictionary folder at the place specified, with
        # "folder_name" as the key and "folder_to_add" as the value
        if self.current_path_is_root():
            target_folder.add_folder(folder_name, self.current_path + folder_name)
        else:
            target_folder.add_folder(folder_name, self.current_path + "/" + folder_name)

    def add_file_at_location(self, file_name, file_size):
        target_folder = self.target_folder(self.current_path)
        target_folder.add_file(file_name, file_size)

    def parse_command(self, command_to_parse):
        # TEST
        print(command_to_parse)
        is_a_command = False
        if command_to_parse.startswith("$"):
            is_a_command = True
        
        if is_a_command == True:
            split_input = command_to_parse.split(" ")
            if split_input[1] == "cd":
                self.change_path(split_input[2])
        # If the prompt is not a command, then it only has two parts to it, though
        # these can either be files or folders.
        else:
            signifier, name = command_to_parse.split(" ")
            if str(signifier).isdigit():
                print("File '{}' created".format(name))
                self.add_file_at_location(name, int(signifier))
            elif str(signifier) == "dir":
                print("Folder '{}' created".format(name))
                self.add_folder_at_location(name)



    # An intentionally recursive method that goes through and double-checks
    # the file sizes on all of the folders, to ensure accuracy.
    def update_folder_sizes(self, target_folder):
        for entry in target_folder.contents:
            if isinstance(entry, Folder):
                entry.calculate_size()
                self.update_folder_sizes(entry)
        # Have to run this twice to make sure the highest-level folders get
        # The proper values
        for entry in target_folder.contents:
            if isinstance(entry, Folder):
                entry.calculate_size()
                self.update_folder_sizes(entry)

    def print_directory(self, target_folder):
        start_level = 0
        for entry in target_folder.contents:
            if isinstance(entry, Folder):
                entry.print_folder(start_level)

    # An intentionally recursive method that should iterate through every folder 
    # and, eventually, return the answer for problem A - that is, the sum of the 
    # file sizes of all folders at or under 100,000 bytes.
    def scan_for_solution_one(self, folder_to_scan):
        folder_sum_total = 0
        for entry in folder_to_scan.contents:
            if isinstance(entry, Folder):
                if entry.test_size(100000) == True:
                    folder_sum_total += entry.get_size()
                folder_sum_total += self.scan_for_solution_one(entry)
        return folder_sum_total
    
    # Again, scan through the documents 
    def scan_for_solution_two(self, folder_to_scan):
        # Now, set variables including the size we desire the drive to be at,
        # the current size of the drive and a list of potential choices
        # MAX_CAPACITY = 70000000
        TARGET_SIZE = 40000000
        current_size = self.drive.get_size()
        potential_choices = []
        for entry in folder_to_scan.contents:
            if isinstance(entry, Folder):
                #TEST
                print("Current entry is " + entry.get_path() + ".")
                print("If deleted, total unused space will be " + str(current_size - entry.get_size()))
                if (current_size - entry.get_size()) <= TARGET_SIZE:
                    potential_choices.append(entry)
                potential_choices.extend(self.scan_for_solution_two(entry))
        potential_choices.sort(key = lambda x: x.size)
        return potential_choices


elf_device = FileStructure()

 
with open("Data Files/Day 7 Data.txt", "r") as input:
    for line in input:
        elf_device.parse_command(line.strip("\n"))
    elf_device.update_folder_sizes(elf_device.drive)
    elf_device.print_directory(elf_device.drive)
    # print("The total is {}".format(elf_device.scan_for_solution_one(elf_device.drive)))
        # First, get the total size of the entire drive with a 'calculate_size'
elf_device.drive.calculate_size()
# TEST
test_list = elf_device.scan_for_solution_two(elf_device.drive)
solution_two_folder = elf_device.scan_for_solution_two(elf_device.drive)[0]
print("The smallest folder to delete and make room is {} at {} bytes."
          .format(solution_two_folder.get_path(), solution_two_folder.get_size()))
