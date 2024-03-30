''' Class HotelStay (GE2.2) '''
from datetime import datetime
from datetime import timedelta
import hashlib

class hotelStay():
    """Gestión de estancia"""
    def __init__(self, idcard, localizer, numdays, room_type):
        self.__alg = "SHA-256"
        self.__type = room_type
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.now()
        self.__arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        numdays = int(numdays)
        delta = timedelta(days=numdays)
        self.__departure = self.__arrival + (delta * 24 * 60 * 60)

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        arrival_str = self.__arrival.strftime("%Y-%m-%d %H:%M:%S")
        departure_str = self.__departure.strftime("%Y-%m-%d %H:%M:%S")
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + arrival_str + \
            ",departure:" + departure_str + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def ic_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value
