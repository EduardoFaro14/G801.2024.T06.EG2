"""Modulo hotelManager"""
import json
import os
from luhn import verify
from src.main.python.uc3m_travel.hotel_management_exception import hotelManagementException
from src.main.python.uc3m_travel.hotel_reservation import hotelReservation
from stdnum.es import nif
from datetime import datetime
from src.main.python.uc3m_travel.hotel_stay import hotelStay

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

        return data

    def validar_formato_fecha(self, cadena):
        if len(cadena) == 10 and cadena[2] == '/' and cadena[5] == '/' and cadena[0].isdigit() and cadena[1].isdigit() and cadena[3].isdigit() and cadena[4].isdigit() and cadena[6:].isdigit():
            return True
        else:
            return False

    def guardar_reserva_en_archivo(self, localizador, idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays):
        # Nombre del archivo donde se guardarán las reservas
        nombre_archivo = r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files\reservas.json"


        nuevo_registro = {
            "Localizer": localizador,
            "CreditCard": creditCardNumber,
            "IdCard": idCard,
            "NameSurname": nameSurname,
            "phoneNumber": phoneNumber,
            "RoomType": roomType,
            "Arrival": arrival,
            "NumDays": numDays
        }
        # Si el archivo no existe, crearlo e inicializarlo con los nuevos datos
        if not os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'w') as f:
                json.dump([nuevo_registro], f, indent=4)
        else:
            with open(nombre_archivo, 'r') as f:
                contenido = json.load(f)
            if not any(registro['localizer'] == localizador for registro in contenido):
                contenido.append(nuevo_registro)
            else:
                raise hotelManagementException("Número reserva erroneo, más de una reserva")
            with open(nombre_archivo, 'w') as f:
                json.dump(contenido, f, indent=4)

    def room_reservation(self, creditCardNumber, idCard, nameSurname, phoneNumber, roomType, arrival, numDays):
        if len(creditCardNumber) > 16:
            raise hotelManagementException("Número de tarjeta de crédito erroneo, más de 16 dígitos")
        if len(creditCardNumber) < 16:
            raise hotelManagementException("Número de tarjeta de crédito erroneo, menos de 16 dígitos")
        for i in creditCardNumber:
            if not i.isdigit():
                raise hotelManagementException("Número de tarjeta de crédito erroneo, tipo de dato")
        if not self.validatecreditcard(creditCardNumber):
            raise hotelManagementException("Número de tarjeta de crédito erroneo, algoritmo de luhn")
        if len(idCard) > 9:
            raise hotelManagementException("Número de DNI erroneo, más de 9 caracteres")
        if len(idCard) < 9:
            raise hotelManagementException("Número de DNI erroneo, menos de 9 caracteres")
        if not nif.is_valid(idCard):
            raise hotelManagementException("Número de DNI erroneo, algoritmo de nift")
        if len(nameSurname) > 50:
            raise hotelManagementException("Nombre y apellido erroneo, más de 50 caracteres")
        if len(nameSurname) < 10:
            raise hotelManagementException("Nombre y apellido erroneo, menos de 10 caracteres")
        for i in range(1, len(nameSurname)):
            if nameSurname[i] == ' ' and nameSurname[i - 1] == ' ':
                raise hotelManagementException("Nombre y apellido erroneo, dos espacios seguidos")
        if nameSurname[0]==' ':
            raise hotelManagementException("Nombre y apellido erroneo, primer caracter es un espacio")
        if nameSurname.endswith(' '):
            raise hotelManagementException("Nombre y apellido erroneo, último caracter es un espacio")
        if not all(i.isalpha() or i.isspace() for i in nameSurname):
            raise hotelManagementException("Nombre y apellido erroneo, tipo de dato")
        if not ' ' in nameSurname:
            raise hotelManagementException("Nombre y apellido erroneo, no hay espacios")
        if len(phoneNumber) > 9:
            raise hotelManagementException("Número de teléfono erroneo, más de 9 dígitos")
        if len(phoneNumber) < 9:
            raise hotelManagementException("Número de teléfono erroneo, menos de 9 dígitos")
        for i in phoneNumber:
            if not i.isdigit():
                raise hotelManagementException("Número de teléfono erroneo, tipo de dato")
        if roomType not in ["SINGLE", "DOUBLE", "SUITE"]:
            raise hotelManagementException("Tipo de habitación erronea, no es ni single ni double ni suite")
        if self.validar_formato_fecha(arrival) == False:
            raise hotelManagementException("Fecha de llegada erronea, tipo de dato")
        dd, mm, yyyy = map(int, arrival.split('/'))
        if dd < 1:
            raise hotelManagementException("Fecha de llegada erronea, menos de día 1")
        if mm in [1, 3, 5, 7, 8, 10, 12]:
            if dd > 31:
                raise hotelManagementException("Fecha de llegada erronea, más de 31 días en un mes de 31")
        if mm in [4, 6, 9, 11]:
            if dd > 30:
                raise hotelManagementException("Fecha de llegada erronea, más de 30 días en un mes de 30")
        if mm in [2] and ((yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)):
            if dd > 29:
                raise hotelManagementException("Fecha de llegada erronea, más de 29 días en febrero bisiesto")
        if mm in [2] and not ((yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)):
            if dd > 28:
                raise hotelManagementException("Fecha de llegada erronea, más de 28 días en febrero no bisiesto")
        if datetime.now() > datetime.strptime(arrival, '%d/%m/%Y'):
            raise hotelManagementException("Fecha de llegada erronea, fecha anterior a la actual")
        if not numDays.isdigit():
            raise hotelManagementException("Número de días erroneo, tipo de dato")
        numeroDias = int(numDays)
        if numeroDias < 1:
            raise hotelManagementException("Número de días erroneo, menos de 1")
        if numeroDias > 10:
            raise hotelManagementException("Número de días erroneo, más de 10")

        reserva_hotel = hotelReservation(idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays)
        localizador = reserva_hotel.localizer
        self.guardar_reserva_en_archivo(localizador, idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays)
        return localizador

    def guest_arrival(self, input_file):
        try:
            # Lee el archivo dado  y verificar que existe y está en formato JSON
            with open(input_file.json, 'r') as f:
                datosReservaf2 = json.load(f)
        except FileNotFoundError:
            raise hotelManagementException("No se encuentra el archivo reservasf2.json")
        except json.JSONDecodeError:
            raise hotelManagementException("El archivo de reservasf2 no está en formato JSON")

            # Verificar si el JSON tiene el Localizer y el IdCard
        if "Localizer" not in datosReservaf2 or "IdCard" not in datosReservaf2:
            raise hotelManagementException("Error, reservasf2.json no tiene Localizer o IdCard")

        localizer = datosReservaf2["Localizer"]
        idCard = datosReservaf2["IdCard"]

        # verificar que el localizador fue almacenado en el fichero de reservas y
        # que el localizador coincide con los datos que estaban en el fichero
        try:
            with open(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files\reservas.json", 'r') as f:
                datosReservaf1 = json.load(f)
        except FileNotFoundError:
            datosReservaf1 = {}

        localizer2 = datosReservaf1["Localizer"]
        idCard2 = datosReservaf1["IdCard"]
        numDays = datosReservaf1["numDays"]
        roomType = datosReservaf1["roomType"]

        if localizer != localizer2:
            raise hotelManagementException("El localizador de reservaf2 no se corresponde con el localizador en el archivo de reservaf1")

        if idCard != idCard2:
            raise hotelManagementException("El DNI de reservaf2 no corresponde con el DNI de reservaf1")

        hotelStay = hotelStay(idCard2, localizer2, numDays, roomType)
        datosReservaFinal = {
            "Localizer": localizer2,
            "IdCard": idCard2,
            "RoomType": roomType,
            "Arrival": hotelStay.arrival,
            "Departure": hotelStay.departure,
            "roomKey": hotelStay.room_key
        }



