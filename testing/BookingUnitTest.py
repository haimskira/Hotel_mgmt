import unittest
from ..backend.Class_booking import *
bfile_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Booking.csv')


class TestBooking(unittest.TestCase):

    def test_book_room(self):
        # Test booking a room with valid input
        arrival_date = "01-01-2022"
        departure_date = "03-01-2022"
        room_id = 1
        cust_id = 1
        result = Booking.book_room(arrival_date, departure_date, room_id, cust_id)
        self.assertTrue(result)

    def test_invalid_c_id(self):
        # Test booking a room with a customer ID that does not exist
        cust_id = 999
        arrival_date = "01-01-2022"
        departure_date = "03-01-2022"
        room_id = 1
        result = Booking.book_room(arrival_date, departure_date, room_id, cust_id)
        self.assertFalse(result)

    def test_invalid_room_id(self):
        # Test booking a room with a room ID that does not exist
        room_id = 999
        cust_id = 1
        arrival_date = "01-01-2022"
        departure_date = "03-01-2022"
        result = Booking.book_room(arrival_date, departure_date, room_id, cust_id)
        self.assertFalse(result)

    def test_invalid_dates(self):
        # Test booking a room with arrival and departure date that overlap with an existing booking
        arrival_date = "05-01-2022"
        departure_date = "07-01-2022"
        room_id = 1
        cust_id = 1
        # create a new booking to test with
        Booking.check_date("02-01-2022", "04-01-2022", room_id)
        # Try booking the same room with overlapping dates
        result = Booking.book_room(arrival_date, departure_date, room_id, cust_id)
        self.assertFalse(result)

    def test_remove_booking(self):
        room_id = 1
        cust_id = 1
        with open(bfile_path, 'r+') as f:
            table = f.readlines()
        for i, row in enumerate(table):
            if str(room_id) == row.strip().split(",")[0] and str(cust_id) == row.strip().split(",")[1]:
                print("remove booking: ", table[i])
                del table[i]
                break
        else:
            print("room not found")
        with open(bfile_path, 'w+') as f:
            for rows in table:
                f.write(rows)


