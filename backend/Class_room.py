import os
import csv
file_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Rooms.csv')

class Room:

    def __init__(self, room_type, room_id, room_size, capacity, num_of_beds, price):
        self.room_type = room_type
        self.room_id = room_id
        self.room_size = room_size
        self.capacity = capacity
        self.num_of_beds = num_of_beds
        self.price = price

    @staticmethod
    def load_from_file():
        import json
        f = open(r'../database/rooms.json')
        data = json.load(f)
        for room in data['rooms']:
            print(room)
        return room

    def add_new_room(self, room_id):
        # Check if a room with the same id already exists
        with open(file_path, 'r+') as f:
            lines = f.readlines()
            room_exists = False
            for line in lines[1:]:
                a = line.strip().split(",")
                if a[0] == room_id:
                    room_exists = True
                    break
        # If the room does not exist, add it to the list of rooms
        if not room_exists:
            with open(file_path, 'a+', newline='') as file_name:
                writer = csv.writer(file_name)
                if int(self) == 1:
                    writer.writerow([room_id, "Basic"])
                    print("Room Basic added successfully!")
                elif int(self) == 2:
                    writer.writerow([room_id, "Deluxe"])
                    print("Room Delux added successfully!")
                elif int(self) == 3:
                    writer.writerow([room_id, "Suite"])
                    print("Room Suite added successfully!")
                else:
                    print("invalied room type")
        else:
            print("Error: Room already exists.")

    @staticmethod
    def display_all_rooms():
        with open(file_path, 'r+', newline='') as file_name:
            read = file_name.readlines()
            for line in read:
                lines = line.strip().split(',')
                print(lines)

    def find_room_by_type(self):
        with open(file_path, 'r+') as fn:
            reader = fn.readlines()
            if self == "1":
                r_type = 'Basic'
            elif self == "2":
                r_type = 'Deluxe'
            elif self == "3":
                r_type = "Suite"
            for line in reader[1:]:
                r_line = line.strip().split(',')
                if r_line[1] == r_type:
                    print(r_line,"\n")

    def find_room_by_number(self):
        with open(file_path, 'r+') as fn:
            reader = fn.readlines()
            for line in reader[1:]:
                r_type = line.strip().split(',')
                if r_type[0] == self:
                    print(r_type, "\n")

    def remove_room(self):
        with open(file_path, 'r+') as f:
            table = f.readlines()
        for i, row in enumerate(table):
            if self == row.strip().split(",")[0]:
                del table[i]
                print("Room deleted succefully")
        with open(file_path, 'w+') as f:
            for row in table:
                f.write(row)

