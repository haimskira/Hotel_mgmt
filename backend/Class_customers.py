import csv
import re
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'Customer.csv')

class Customer:
    def __init__(self, c_id, name: str, address, city, email, age: str):
        self.c_id = c_id
        self.name = name
        self.address = address
        self.city = city
        self.email = email
        self.age = age

    @staticmethod
    def check_mail(mail):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, mail):
            print("Valid email")
        else:
            print("Invalid email")
            quit()


    @staticmethod
    def check_age(age):
        if int(age) < 18 or int(age) > 120:
            print("invalid age")
            quit()



    def add_customer(self):
        Customer.check_mail(self.email)
        Customer.check_age(self.age)
        print("ADD Succesfully")
        with open(file_path) as customercsv:
            lines = customercsv.readlines()
            customer_not_exist = False
            for line in lines[1:]:
                a = line.strip().split(",")
                if int(a[0]) == int(self.c_id):
                    customer_not_exist = True
                    break
        if not customer_not_exist:
            with open(file_path, 'a', newline='') as customercsv:
                writer = csv.writer(customercsv)
                writer.writerow([self.c_id, self.name.lower(), self.address, self.city, self.email, self.age])
        else:
            print("customer ID allredy exist")

    def find_customer_by_name(self):
        with open(file_path) as customercsv:
            lines = customercsv.readlines()
            for line in lines[1:]:
                name = line.strip().split(",")
                if name[1] == str(self):
                    print(name)
                    break

    def remove_customer(self):
        with open(file_path, 'r+') as f:
            table = f.readlines()
        for i, row in enumerate(table):
            if str(self) == row.strip().split(",")[0]:
                del table[i]
        with open(file_path, 'w+') as f:
            for row in table:
                f.write(row)

    @staticmethod
    def display_all_customer():
        with open(file_path) as file_name:
            read = file_name.readlines()
            for line in read:
                lines = line.strip().split(',')
                print(lines)