import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv")


class Hotel:
    firm = "Blackrock Real Estate Group"  # Class variable

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """books a hotel by changing its availability to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """checks if the hotel is unoccupied or not booked"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):  # Class method
        return len(data)

    def __eq__(self, other):  # Magic method
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):  # Class inheriting the abstract must have instances of its method or function
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def generate(self):
        content = f"""
        You've successfully booked your reservation! 
        Your booking details are:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel_name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 10


hotel1 = Hotel(hotel_id=134)
hotel2 = Hotel(hotel_id=188)

print(hotel1.name)
print(hotel2.name)

print(hotel1.firm)  # Class variable is accessible by all instances
print(hotel2.firm)  # The print function will give the same result

print(Hotel.firm)  # It is created immediately under the class b4 object definitions

print(hotel1.available())  # Instant object are specific to an instant
print(Hotel.get_hotel_count(data=df))  # Class objects are related to the class but not specific to any instant

ticket = ReservationTicket(customer_name="john smith  ", hotel_name=hotel1)
print(ticket.customer_name)
print(ticket.generate())

print(ticket.convert(10))
