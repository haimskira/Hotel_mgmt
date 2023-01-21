import csv
import os
from datetime import datetime

bfile_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Booking.csv')
cfile_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Customer.csv')
rfile_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Rooms.csv')


class Booking:

    @staticmethod
    def check_custumer(cust_id):
        with open(cfile_path, 'r') as cfile:
            lines = cfile.readlines()
            for line in lines[1:]:
                res = line.strip().split(',')
                if int(res[0]) == cust_id:
                    return True
                    break

        #        return print("customer not found, add new customer or add new customer id")

    @staticmethod
    def check_room(room_id):
        with open(rfile_path, 'r') as roomfile:
            roomlines = roomfile.readlines()
            for line in roomlines[1:]:
                roomres = line.strip().split(',')
                if int(roomres[0]) == room_id:
                    return True
                    break

    @staticmethod
    def check_date(arrival_date, departure_date, room_id):
        from datetime import datetime
        date_format = "%d-%m-%Y"

        at = datetime.strptime(arrival_date, date_format)
        dt = datetime.strptime(departure_date, date_format)
        with open(bfile_path, 'r') as file:
            bookingfile = file.readlines()
            for line in bookingfile[1:]:
                book_id = line.strip().split(',')
                if int(book_id[0]) == room_id:
                    ckeck_date = datetime.strptime(book_id[2], date_format)
                    if at <= ckeck_date <= dt:
                        return False
                        break
            else:
                 return True

    @staticmethod
    def check_min_nights(arrival_date, departure_date, room_id):
        from datetime import datetime
        date_format = "%d-%m-%Y"
        with open(rfile_path, 'r') as roomfile:
            roomlines = roomfile.readlines()
            for line in roomlines[1:]:
                roomres = line.strip().split(',')
                if int(roomres[0]) == room_id:
                    room_type = roomres[1]
                    if room_type == "Basic":
                        min_nights = 1
                    elif room_type == "Deluxe":
                        min_nights = 2
                    else:
                        min_nights = 3

        num_nights = (datetime.strptime(departure_date, date_format) - datetime.strptime(arrival_date, date_format)).days
        if num_nights < min_nights:
            print(f"Minimum booking time for a {room_type} room is {min_nights} nights.")
            return False
        else:
            return True

    @staticmethod
    def book_room(arrival_date, departure_date, room_id, cust_id):
        if Booking.check_room(room_id):
            if Booking.check_custumer(cust_id):
                if Booking.check_date(arrival_date, departure_date, room_id):
                    if Booking.check_min_nights(arrival_date, departure_date, room_id):
                        from datetime import datetime
                        date_format = "%d-%m-%Y"
                        with open(rfile_path, 'r') as roomfile:
                            roomlines = roomfile.readlines()
                            for line in roomlines[1:]:
                                roomres = line.strip().split(',')
                                if int(roomres[0]) == room_id:
                                    room_type = roomres[1]
                                    if room_type == "Basic":
                                        price = 1000
                                    elif room_type == "Deluxe":
                                        price = 2000
                                    else:
                                        price = 3000

                            num_nights = (datetime.strptime(departure_date, date_format) - datetime.strptime(arrival_date,
                                                                                                            date_format)).days
                            total_price = num_nights * price
                            with open(bfile_path, 'a', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow([room_id, cust_id, arrival_date, departure_date, total_price])
                                print("room successfully booked")
                    else:
                        print("Please choose another room or another period of time ")
                else:
                    print("room is occupied on those dates, choose other dates")
            else:
                print("customer not found, add new customer or add new customer id")
        else:
            print('Room Not Found')

    @staticmethod
    def check_logic_dates(ArrivalDate, DepartureDate):
        from datetime import datetime
        date_format = "%d-%m-%Y"

        at = datetime.strptime(ArrivalDate, date_format)
        dt = datetime.strptime(DepartureDate, date_format)
        if dt > at:
            return True
        else:
            print("invaild dates")
            return False

    @staticmethod
    def book_a_room(room_id, cust_id, arrival_date, departure_date):
        if Booking.check_logic_dates(arrival_date, departure_date):
            Booking.check_room(room_id)
            Booking.check_custumer(cust_id)
            Booking.check_date(arrival_date, departure_date, room_id)
            Booking.check_min_nights(arrival_date, departure_date, room_id)
            Booking.book_room(arrival_date, departure_date, room_id, cust_id)

    @staticmethod
    def remove_booking(room_id, cust_id):
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

    @staticmethod
    def display_all_booking():
        with open(bfile_path) as file_name:
            read = file_name.readlines()
            for line in read:
                lines = line.strip().split(',')
                print(lines)

    @staticmethod
    def booked_rooms_for_aspefic_date(arrival_date, departure_date):
        if Booking.check_logic_dates(arrival_date, departure_date):
            Booking.display_booked_room_for_dates(arrival_date, departure_date)



    @staticmethod
    def display_booked_room_for_dates(arrival_date, departure_date):
        date_format = "%d-%m-%Y"

        at = datetime.strptime(arrival_date, date_format)
        dt = datetime.strptime(departure_date, date_format)

        with open(bfile_path, 'r') as file:
            bookingfile = file.readlines()
            for line in bookingfile[1:]:
                booked = line.strip().split(",")
                ckeck_date_at = datetime.strptime(booked[2], date_format)
                ckeck_date_dt = datetime.strptime(booked[3], date_format)
                if at == ckeck_date_at and dt == ckeck_date_dt:
                    print()
                    print( booked)



    @staticmethod
    def check_available_date(ArrivalDate, DepartureDate):
        Booking.avlibale_rooms_from_file()
        from datetime import datetime
        date_format = "%d-%m-%Y"

        at = datetime.strptime(ArrivalDate, date_format)
        dt = datetime.strptime(DepartureDate, date_format)

        with open(bfile_path, 'r') as file:
            bookingfile = file.readlines()

            for line in bookingfile[1:]:
                booked = line.strip().split(",")
                ckeck_date_at = datetime.strptime(booked[2], date_format)
                ckeck_date_dt = datetime.strptime(booked[3], date_format)
                if not at <= ckeck_date_at <= dt or not at <= ckeck_date_dt <= dt:
                    with open(rfile_path, 'r') as roomfile:
                        roomlines = roomfile.readlines()
                        for line in roomlines[1:]:
                            roomres = line.strip().split(',')
                            if booked[0] == roomres[0]:
                                print(roomres[0], roomres[1])

    @staticmethod
    def avlibale_rooms_from_file():
        rooms_ls = []
        booked_ls = []
        res3 = []
        with open(rfile_path, 'r') as roomfile:
            roomlines = roomfile.readlines()
            for line in roomlines[1:]:
                roomres = line.strip().split(',')
                rooms_ls.append(roomres[0])

        with open(bfile_path, 'r') as file:
            bookingfile = file.readlines()
            for line in bookingfile[1:]:
                bookeed = line.strip().split(',')
                booked_ls.append(bookeed[0])

        for i in rooms_ls:
            if i not in booked_ls:
                res3.append(i)

        with open(rfile_path, 'r') as roomfile:
            roomlines = roomfile.readlines()
            for line in roomlines[1:]:
                roomres = line.strip().split(',')
                for j in res3:
                    if roomres[0] == j:
                        print(roomres[0], roomres[1])