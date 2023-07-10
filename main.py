import pandas as pd

df = pd.read_csv("hotels.csv")
df_cards = pd.read_csv("cards.csv").to_dict(orient="records")


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder_name, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder_name, "cvc": cvc}
        if card_data in df_cards:
            return True


print(df)
hotel_ID = int(input("Enter the id of the hotel: "))
hotel = Hotel(hotel_ID)

if hotel.available():
    number = int(input("Enter the 16 digit number in front of your card: "))
    expiration = input("Enter the expiry date of your card: ")
    cvc = int(input("Enter the 3 digit number on the back of your card: "))
    holder = input("Enter your name as it appears on the card: ")
    credit_card = CreditCard(number=number)
    if credit_card.validate(expiration=expiration, cvc=cvc,
                            holder_name=holder):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_name=hotel.name)
        print(reservation_ticket.generate())
    else:
        print("Couldn't validate your card, review your card details or try another card")
else:
    print("Hotel is unavailable")
