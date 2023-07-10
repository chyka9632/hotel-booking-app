import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
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


class ReservationTicket:
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def generate(self):
        content = f"""
        You've successfully booked your reservation! 
        Your booking details are:
        Name: {self.customer_name}
        Hotel name: {self.hotel_name}
        """
        return content


print(df)
hotel_ID = int(input("Enter the id of the hotel: "))
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_name=hotel.name)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available")
