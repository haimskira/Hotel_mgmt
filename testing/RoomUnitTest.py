import unittest
from ..backend.Class_room import *
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Rooms.csv')


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_id = "1"
        self.room_type = "1"

    def test_add_new_room(self):
        # Test adding a new room

        Room.add_new_room(self.room_type, self.room_id)
        with open(file_path, 'r+') as file_name:
            read = file_name.readlines()
            for line in read[1:]:
                lines = line.strip().split(',')
                if lines[0] == str(self.room_id):
                    self.assertEqual(lines[1], self.room_type)

        # Test adding a room with an already existing id
        self.assertRaises(Exception, Room.add_new_room, self.room_id, self.room_type)

    def test_display_all_rooms(self):
        # Test displaying all rooms
        Room.display_all_rooms()
        with open(file_path, 'r+') as file_name:
            read = file_name.readlines()
            self.assertGreater(len(read), 1)

    def test_find_room_by_type(self):
        # Test finding a room by type
        Room.find_room_by_type(self.room_type)
        with open(file_path, 'r+') as file_name:
            read = file_name.readlines()
            for line in read[1:]:
                lines = line.strip().split(',')
                if lines[1] == self.room_type:
                    self.assertEqual(lines[0], str(self.room_id))

    def test_find_room_by_number(self):
        # Test finding a room by room number
        Room.find_room_by_number(self.room_id)
        with open(file_path, 'r+') as file_name:
            read = file_name.readlines()
            for line in read[1:]:
                lines = line.strip().split(',')
                if lines[0] == str(self.room_id):
                    self.assertEqual(lines[1], self.room_type)

    def test_remove_room(self):
        # Test removing a room
        with self.assertLogs() as log:
            Room.remove_room(self.room_id)
            self.assertIn('Room deleted succefully', log.output[0])
        with open(file_path, 'r+') as file_name:
            read = file_name.readlines()
            for line in read[1:]:
                lines = line.strip().split(',')
                self.assertNotEqual(lines[0], str(self.room_id))


if __name__ == '__main__':
    unittest.main()

