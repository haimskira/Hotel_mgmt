import unittest
from ..backend.Class_customers import *
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Customer.csv')


class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Create a test customer for use in the tests
        self.test_customer = Customer(1, "John Doe", "123 Main St", "New York", "john.doe@example.com", "30")
        self.c_id = 1

    def test_add_customer(self):
        # Test adding a new customer
        self.test_customer.add_customer()
        with open(file_path) as customercsv:
            reader = csv.reader(customercsv)
            for row in reader:
                if row[0] == "1":
                    self.assertEqual(row[1], "John Doe")
                    self.assertEqual(row[2], "123 Main St")
                    self.assertEqual(row[3], "New York")
                    self.assertEqual(row[4], "john.doe@example.com")
                    self.assertEqual(row[5], "30")
                    break
        # Test adding a customer with an already existing id
        self.test_customer.add_customer()
        with open(file_path) as customercsv:
            reader = csv.reader(customercsv)
            count = sum(1 for row in reader if row[0] == "1")
            self.assertEqual(count, 1)

    def test_find_customer_by_name(self):
        # Test finding a customer by name
        self.test_customer.find_customer_by_name()
        with open(file_path) as customercsv:
            reader = csv.reader(customercsv)
            for row in reader:
                if row[1] == "John Doe":
                    print(row)
                    self.assertEqual(row[0], "1")
                    break


    def test_remove_customer(self):
        self.c_id = 1
        with open(file_path, 'r+') as f:
            table = f.readlines()
        for i, row in enumerate(table):
            if str(self.c_id) == row.strip().split(",")[0]:
                del table[i]
        with open(file_path, 'w+') as f:
            for row in table:
                f.write(row)

    def test_display_all_customer(self):
        # Test displaying all customers
        with open(file_path) as file_name:
            read = file_name.readlines()
            for line in read:
                lines = line.strip().split(',')
                print(lines)

if __name__ == '__main__':
    unittest.main()
