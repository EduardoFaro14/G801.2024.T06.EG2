"""Este módulo es reservation"""

import hashlib
from datetime import datetime


class hotelReservation:
    """Reservas"""

    def __init__(self, id_card, creditcard_numb, arrival, name_and_surname,
                 phone_number, room_type, num_days):
        self.credit_card_number = creditcard_numb
        self.__idcard = id_card
        self.__arrival = arrival
        self.name_surname = name_and_surname
        self.__phonenumber = phone_number
        self.__roomtype = room_type
        self.__num_days = num_days

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        jsoninfo = {"id_card": self.__idcard,
                    "name_surname": self.name_surname,
                    "credit_card": self.credit_card_number,
                    "phone_number:": self.__phonenumber,
                    "arrival_date": self.__arrival,
                    "num_days": self.__num_days,
                    "room_type": self.__roomtype,
                    }
        return "HotelReservation:" + jsoninfo.__str__()

    @property
    def credit_card(self):
        """devuelve el número de tarjeta de crédito"""
        return self.credit_card_number

    @credit_card.setter
    def credit_card(self, value):
        """Pone el valor en el número de tarjeta de crédito"""
        self.credit_card_number = value

    @property
    def id_card(self):
        """Devuelve el id"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        """Pone el valor en el id"""
        self.__idcard = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return hashlib.md5(str(self).encode()).hexdigest()
