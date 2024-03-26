"""Modulo hotelManager"""
import json
import os
from luhn import verify
from uc3m_travel.hotel_management_exception import hotelManagementException
from uc3m_travel.hotel_reservation import hotelReservation
from stdnum.es import nif
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

        return data

    def validar_formato_fecha(self, cadena):
        try:
            # Intentamos analizar la cadena como una fecha en el formato especificado
            datetime.strptime(cadena, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def guardar_reserva_en_archivo(self, localizador, idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays):
        # Nombre del archivo donde se guardarán las reservas
        nombre_archivo = "reservas.json"

        # Si el archivo no existe, crearlo e inicializarlo con una lista vacía
        if not os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'w') as f:
                json.dump([], f)

        # Leer las reservas existentes desde el archivo
        reservas = self.readdatafrom_json(nombre_archivo)
        for i in reservas:
            if i["localizer"] == localizador:
                return True
        # Agregar la nueva reserva al archivo de reservas
        reserva_info = {
            "localizer": localizador,
            "CreditCard": creditCardNumber,
            "IdCard": idCard,
            "NameSurname": nameSurname,
            "phoneNumber": phoneNumber,
            "RoomType": roomType,
            "Arrival": arrival,
            "NumDays": numDays,
        }

        reservas.append(reserva_info)

        # Guardar las reservas actualizadas en el archivo
        with open(nombre_archivo, 'w') as f:
            json.dump(reservas, f, indent=4)
        return True

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
        if self.validar_formato_fecha(arrival) == False:
            raise hotelManagementException("Fecha de llegada erronea, tipo de dato")
        if datetime.now() > datetime.strptime(arrival, '%d/%m/%Y'):
            raise hotelManagementException("Fecha de llegada erronea, fecha anterior a la actual")
        if numDays > 10:
            raise hotelManagementException("Número de días erroneo, más de 10")
        if numDays < 1:
            raise hotelManagementException("Número de días erroneo, menos de 1")
        if not numDays.isdigit():
            raise hotelManagementException("Número de días erroneo, tipo de dato")

        reserva_hotel = hotelReservation(idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays)
        localizador = reserva_hotel.localizer
        self.guardar_reserva_en_archivo(localizador, idCard, creditCardNumber, arrival, nameSurname, phoneNumber, roomType, numDays)
        return localizador

    def guest_arrival(self, input_file, stays_file):
        try:
            # Lee el archivo de entrada y obtener los datos (verificar existencia y formato JSON)
            data = self.readdatafrom_json(input_file)
        except hotelManagementException as e:
            raise hotelManagementException(str(e))

        # Verificar si el JSON tiene la estructura esperada
        if "Localizer" not in data or "IdCard" not in data:
            raise hotelManagementException("El JSON no tiene la estructura esperada.")

        localizer = data["Localizer"]
        idcard = data["IdCard"]

        # Verificar si el localizador existe en el fichero de estancias
        try:
            with open(stays_file, 'r') as file:
                stays_data = json.load(file)
        except FileNotFoundError:
            stays_data = {}

        if localizer not in stays_data:
            raise hotelManagementException("El localizador no se corresponde con los datos almacenados.")

        # Obtener los datos de la estancia del localizador
        stay_data = stays_data[localizer]

        if idcard != stay_data["idcard"]:
            raise hotelManagementException("El DNI no se corresponde con los datos almacenados.")

        # Obtener la fecha de llegada esperada
        expected_arrival = stay_data["arrival"]

        # Verificar si la fecha de llegada coincide con la esperada
        if expected_arrival != data["arrival"]:
            raise hotelManagementException("La fecha de llegada no se corresponde con la fecha de reserva.")

        # Crear objeto HotelStay
        hotel_stay = HotelStay(idcard, localizer, 1, stay_data["typ"])

        # Guardar la estancia y la clave de la habitación en el fichero de estancias
        stays_data[localizer]["room_key"] = hotel_stay.room_key
        with open(stays_file, 'w') as file:
            json.dump(stays_data, file, indent=4)

        # Devolver la clave de la habitación
        return hotel_stay.room_key

