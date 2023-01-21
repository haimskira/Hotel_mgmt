# Hotel management system - JB project
This project is for creating a simple system to manage hotel bookings. The system uses three tables: Rooms, Customers, and Bookings. The Rooms table is represented by a Rooms.csv file and contains information such as room size, capacity, number of beds, type (Basic/Deluxe/Suite), and price. The Customers table is represented by a Customers.csv file and contains information such as the customer's name, address, city, email, and age. The Bookings table is represented by a Bookings.csv file and contains information such as the customer ID, room ID, arrival and departure dates, and total price.

The minimum booking time for a room is determined by the room type: Basic rooms have no limitation, Deluxe rooms require at least two nights, and Suite rooms require at least three nights.

A command-line interface (CLI) is to be built for the system. Each entity (Rooms, Customers, and Bookings) should have its own class and module. Unit tests should also be built.
