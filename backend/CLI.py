from Class_room import *
from Class_customers import *
from Class_booking import *



def user_interface():
    while 1:
        print("[1] - Add a new room")

        print("[2] - Add a new customer ")

        print("[3] - Book a room")

        print("[4] - Cancel booking")

        print("[5] - Display all rooms")

        print("[6] - Display all costumers")

        print("[7] - Display all bookings")

        print("[8] - Display booked rooms for a specific date")

        print("[9] - Display available rooms for a specific date")

        print("[10] - Find room by type")

        print("[11] - Find room by number ")

        print("[12] - Find customer by name")

        print("[13] - Remove room")

        print("[14] - Remove customer")

        print("[15] - Display JSON room types")

        print("[0] - .EXIT")

        user_choice = int(input("\nEnter your choice:"))

        if user_choice == 1:
            #  Add a new room

            print("choose a room to add: [1] - Basic, [2] - Deluxe, [3] - Suites:")
            room_type = int(input("Enter the room type: "))
            room_id = input("Enter the room id: ")
            Room.add_new_room(room_type, room_id)

        if user_choice == 2:
            #  Add a new customer
            Name = input("please enter the name:")
            Id = input("please enter the id:")
            Address = input("please enter the address:")
            Email = input("please enter the mail:")
            City = input("please enter the city:")
            Age = input("please enter the age:")
            customer = Customer(Id, Name, Address, City, Email, Age)
            customer.add_customer()

        if user_choice == 3:
            #  Book a room

            room_id = int(input("\nEnter your room id: "))
            cust_id = int(input("\nEnter Customer id: "))
            arrival_date = input('Enter your Arrival Date formatted as DD-MM-YYYY: ')
            departure_date = input('Enter your Departure Date formatted as DD-MM-YYYY: ')

            Booking.book_a_room(room_id, cust_id, arrival_date, departure_date)

        if user_choice == 4:
            #  Cancel booking
            room_id = input("\nEnter your room id: ")
            cust_id = input("\nEnter Customer id: ")
            Booking.remove_booking(room_id, cust_id)

        if user_choice == 5:
            #  Display all rooms
            Room.display_all_rooms()

        if user_choice == 6:
            #  Display all customers
            Customer.display_all_customer()

        if user_choice == 7:
            #  Display all bookings
            Booking.display_all_booking()

        if user_choice == 8:
            #  Display booked rooms for a specific date
            arrival_date = input('Enter your Arrival Date formatted as DD-MM-YYYY: ')
            departure_date = input('Enter your Departure Date formatted as DD-MM-YYYY: ')
            Booking.booked_rooms_for_aspefic_date(arrival_date, departure_date)

        if user_choice == 9:
                #  Display available rooms for a specific date

                arrival_date = input('Enter your Arrival Date formatted as DD-MM-YYYY: ')
                departure_date = input('Enter your Departure Date formatted as DD-MM-YYYY: ')
                Booking.check_available_date(arrival_date, departure_date)

        if user_choice == 10:
            #  Find room by type

            print("choose a room to display by room type: [1] - Basic, [2] - Deluxe, [3] - Suites:")
            room_type = input("Enter the room type: ")
            Room.find_room_by_type(room_type)

        if user_choice == 11:
            #  Find room by number

            print("choose a room to display by room number: ")
            room_id = input("Enter the room number: ")
            Room.find_room_by_number(room_id)

        if user_choice == 12:
            #  Find customer by name
            print("find customer by name")
            c_name = input("Enter customer name: ").lower()
            Customer.find_customer_by_name(c_name)

        if user_choice == 13:
            #  Remove room
            room_id = input("Enter the room number: ")
            Room.remove_room(room_id)

        if user_choice == 14:
            #  Remove customer
            cust_id = input("Enter the customer id: ")
            Customer.remove_customer(cust_id)

        if user_choice == 15:
            Room.load_from_file()

        if user_choice == 0:
            #  EXIT
            quit()


user_interface()
