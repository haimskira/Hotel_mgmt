from ..backend.Class_room import *
from ..backend.Class_customers import *
from ..backend.Class_booking import *

# 1
Room.add_new_room(1, "155")
Room.add_new_room(5, "123")
Room.add_new_room(5, "255")
# 2
customer = Customer("1234512345", "moki", "hetzikl", "lod", "qwe@qwe.com", "29")
Customer.add_customer(customer)
# 3
Booking.book_a_room(189, 5546, "01-02-2022", "05-02-2022")
# 4
Booking.remove_booking("190", " 5546")
# 5
Room.display_all_rooms()
# 6
Customer.display_all_customer()
# 7
Booking.display_all_booking()
# 8
Booking.booked_rooms_for_aspefic_date("01-02-2022", "05-02-2022")
# 9
Booking.check_available_date("01-02-2022", "05-02-2022")
# 10
Room.find_room_by_type("1")
# 11
Room.find_room_by_number("453")
# 12
c_name = input("Enter customer name: ").lower()
Customer.find_customer_by_name(c_name)
# 13
Room.remove_room("453")
# 14
Customer.remove_customer("12345645")
