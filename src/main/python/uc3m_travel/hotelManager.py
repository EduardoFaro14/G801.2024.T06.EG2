import json
from luhn import verify
from .hotelManagementException import hotelManagementException
from .hotelReservation import hotelReservation
class hotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        """valida la tarjeta"""
        return verify(x)
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
    def readdatafrom_json(self, fi):
        """leer de JSON"""
        try:
            with open(fi, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = hotelReservation(id_card="12345678Z", creditcard_numb=c,
                                   name_and_surname="John Doe",
                                   phone_number=p, room_type="single", num_days=3)
        except KeyError as e:
            raise hotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelManagementException("Invalid credit card number")

        # Close the file
        return req
