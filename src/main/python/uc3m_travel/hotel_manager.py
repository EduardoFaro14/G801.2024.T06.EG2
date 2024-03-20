"""Modulo hotelManager"""
import json
import os
from luhn import verify
from .hotel_management_exception import hotelManagementException
from .hotel_reservation import hotelReservation
from stdnum import es
from datetime import datetime

class hotelManager:
    """ Esta clase comprueba que la tarjeta sea válida y lee los datos de json"""
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

    def validar_formato_fecha(self, cadena):
        try:
            # Intentamos analizar la cadena como una fecha en el formato especificado
            datetime.strptime(cadena, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def guardar_reserva_en_archivo(self, reserva):
        # Nombre del archivo donde se guardarán las reservas
        nombre_archivo = "reservas.json"

        # Si el archivo no existe, crearlo e inicializarlo con una lista vacía
        if not os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'w') as f:
                json.dump([], f)

        # Leer las reservas existentes desde el archivo
        with open(nombre_archivo, 'r') as f:
            reservas = json.load(f)

        # Agregar la nueva reserva al archivo de reservas
        reserva_info = {
            "localizer": reserva.localizer,
            "data": str(reserva)
        }
        reservas.append(reserva_info)

        # Guardar las reservas actualizadas en el archivo
        with open(nombre_archivo, 'w') as f:
            json.dump(reservas, f, indent=4)

    def room_reservation(self, creditCardNumber, idCard, nameSurname, phoneNumber, roomType, arrival, numDays):
        if (self.validatecreditcard(creditCardNumber) and es.nif.validate(idCard) and 10 <= len(nameSurname) <= 50 and len(nameSurname.split()) >= 2 and len(phoneNumber) == 9 and (roomType == "single" or roomType == "double" or roomType == "suite") and self.validar_formato_fecha(arrival) and 1 <= numDays <= 10):
            localizador = hotelReservation(idCard, creditCardNumber, nameSurname, phoneNumber, roomType, numDays)
            self.guardar_reserva_en_archivo(localizador)
            return localizador
        else:
            print("Error, algo falla")
            raise hotelManagementException("Error en la reserva")