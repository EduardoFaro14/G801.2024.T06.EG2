"""Modulo hotelManager"""
import json
import os
import re

from datetime import datetime
from luhn import verify
from stdnum.es import nif
from uc3m_travel.hotel_management_exception import hotelManagementException
from uc3m_travel.hotel_reservation import hotelReservation
from uc3m_travel.hotel_stay import hotelStay


class hotelManager:
    """ Esta clase comprueba que la tarjeta sea válida y lee los datos de json"""

    def __init__(self):
        pass

    def validatecreditcard(self, x):
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
            raise hotelManagementException("El archivo de "
                                           "reservasf2 no está en formato JSON") from e

        return data
    def validar_formato_fecha(self, cadena):
        '''Función para saber que el formato de la fecha es el correcto'''
        return (len(cadena) == 10 and cadena[2] == '/' and cadena[5] == '/'
                and cadena[0].isdigit() and cadena[
                1].isdigit() and cadena[3].isdigit()
                and cadena[4].isdigit() and cadena[6:].isdigit())

    def guardar_reserva2_en_archivo\
    (self, localizador, id_card, room_type, arrival, departure, room_key):
        '''Función para guardar datos en reservas2'''
        # Nombre del archivo donde se guardarán las reservas
        nombreArchivo = (r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri"
                         r"\EG2\src\main\python\json_files\reservas2.json")

        # arrival = str(arrival[0].isoformat())
        # departure = departure[0].isoformat()
        arrivalstr = arrival.strftime("%Y-%m-%d")
        departurestr = departure.strftime("%Y-%m-%d")
        datosReservaFinal = {
            "Localizer": localizador,
            "IdCard": id_card,
            "RoomType": room_type,
            "Arrival": arrivalstr,
            "Departure": departurestr,
            "roomKey": room_key
        }

        # Si el archivo no existe, crearlo e inicializarlo con los nuevos datos
        if not os.path.exists(nombreArchivo):
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump(datosReservaFinal, f, indent=4)
        else:
            with open(nombreArchivo, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
            if not any(registro['localizer'] == localizador for registro in contenido):
                contenido.append(datosReservaFinal)
            else:
                raise hotelManagementException("Número reserva erroneo, más de una reserva")
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump(contenido, f, indent=4)

    def guardar_reserva_en_archivo\
    (self, localizador, id_card,
    credit_card_number, arrival, name_surname, phone_number,
    room_type, num_days):
        '''Función para guardar datos en reservas'''
        # Nombre del archivo donde se guardarán las reservas
        nombreArchivo = (r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri"
                         r"\EG2\src\main\python\json_files\reservas.json")

        nuevoRegistro = {
            "Localizer": localizador,
            "CreditCard": credit_card_number,
            "IdCard": id_card,
            "NameSurname": name_surname,
            "phoneNumber": phone_number,
            "RoomType": room_type,
            "Arrival": arrival,
            "NumDays": num_days
        }
        # Si el archivo no existe, crearlo e inicializarlo con los nuevos datos
        if not os.path.exists(nombreArchivo):
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump([nuevoRegistro], f, indent=4)
        else:
            with open(nombreArchivo, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
            if not any(registro["Localizer"] == localizador for registro in contenido):
                contenido.append(nuevoRegistro)
            else:
                raise hotelManagementException("Número reserva erroneo, más de una reserva")
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump(contenido, f, indent=4)

    def insertar_datos(self, fecha_actual, room_key):
        '''Función para guardar datos en reservas3'''
        nombreArchivo = (r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri"
                         r"\EG2\src\main\python\json_files\reservas3.json")
        nuevoRegistro = {
            "Fecha de Salida": fecha_actual,
            "roomKey": room_key
        }
        # Si el archivo no existe, crearlo e inicializarlo con los nuevos datos

        if not os.path.exists(nombreArchivo):
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump([nuevoRegistro], f, indent=4)
        else:
            try:
                with open(nombreArchivo, 'r', encoding='utf-8') as f:
                    contenido = json.load(f)
            except json.JSONDecodeError as e:
                raise (hotelManagementException
                       ("El archivo de reservas3 no está en formato JSON")) from e
            if not any(registro['roomKey'] == room_key for registro in contenido):
                contenido.append(nuevoRegistro)
            else:
                raise hotelManagementException("Número de roomKey repetido")
            with open(nombreArchivo, 'w', encoding='utf-8') as f:
                json.dump(contenido, f, indent=4)
    def room_reservation\
    (self, credit_card_number, id_card, name_surname
     , phone_number, room_type, arrival, num_days):
        '''Función 1'''
        if len(credit_card_number) > 16:
            raise (hotelManagementException
                   ("Número de tarjeta de crédito erroneo, más de 16 dígitos"))
        if len(credit_card_number) < 16:
            raise (hotelManagementException
                   ("Número de tarjeta de crédito erroneo, menos de 16 dígitos"))
        for i in credit_card_number:
            if not i.isdigit():
                raise (hotelManagementException
                       ("Número de tarjeta de crédito erroneo, tipo de dato"))
        if not self.validatecreditcard(credit_card_number):
            raise (hotelManagementException
                   ("Número de tarjeta de crédito erroneo, algoritmo de luhn"))
        if len(id_card) > 9:
            raise (hotelManagementException
                   ("Número de DNI erroneo, más de 9 caracteres"))
        if len(id_card) < 9:
            raise (hotelManagementException
                   ("Número de DNI erroneo, menos de 9 caracteres"))
        if not nif.is_valid(id_card):
            raise (hotelManagementException
                   ("Número de DNI erroneo, algoritmo de nift"))
        if len(name_surname) > 50:
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, más de 50 caracteres"))
        if len(name_surname) < 10:
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, menos de 10 caracteres"))
        for i in range(1, len(name_surname)):
            if name_surname[i] == ' ' and name_surname[i - 1] == ' ':
                raise (hotelManagementException
                       ("Nombre y apellido erroneo, dos espacios seguidos"))
        if name_surname[0] == ' ':
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, primer caracter es un espacio"))
        if name_surname.endswith(' '):
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, último caracter es un espacio"))
        if not all(i.isalpha() or i.isspace() for i in name_surname):
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, tipo de dato"))
        if not ' ' in name_surname:
            raise (hotelManagementException
                   ("Nombre y apellido erroneo, no hay espacios"))
        if len(phone_number) > 9:
            raise (hotelManagementException
                   ("Número de teléfono erroneo, más de 9 dígitos"))
        if len(phone_number) < 9:
            raise (hotelManagementException
                   ("Número de teléfono erroneo, menos de 9 dígitos"))
        for i in phone_number:
            if not i.isdigit():
                raise (hotelManagementException
                       ("Número de teléfono erroneo, tipo de dato"))
        if room_type not in ["SINGLE", "DOUBLE", "SUITE"]:
            raise (hotelManagementException
                   ("Tipo de habitación erronea, no es ni single ni double ni suite"))
        if self.validar_formato_fecha(arrival) is False:
            raise (hotelManagementException
                   ("Fecha de llegada erronea, tipo de dato"))
        dd, mm, yyyy = map(int, arrival.split('/'))
        if dd < 1:
            raise (hotelManagementException
                   ("Fecha de llegada erronea, menos de día 1"))
        if mm in [1, 3, 5, 7, 8, 10, 12]:
            if dd > 31:
                raise (hotelManagementException
                       ("Fecha de llegada erronea, más de 31 días en un mes de 31"))
        if mm in [4, 6, 9, 11]:
            if dd > 30:
                raise (hotelManagementException
                       ("Fecha de llegada erronea, más de 30 días en un mes de 30"))
        if mm in [2] and ((yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)):
            if dd > 29:
                raise (hotelManagementException
                       ("Fecha de llegada erronea, más de 29 días en febrero bisiesto"))
        if mm in [2] and not ((yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)):
            if dd > 28:
                raise (hotelManagementException
                       ("Fecha de llegada erronea, más de 28 días en febrero no bisiesto"))
        if datetime.now() > datetime.strptime(arrival, '%d/%m/%Y'):
            raise (hotelManagementException
                   ("Fecha de llegada erronea, fecha anterior a la actual"))
        if not num_days.isdigit():
            raise (hotelManagementException
                   ("Número de días erroneo, tipo de dato"))
        numeroDias = int(num_days)
        if numeroDias < 1:
            raise (hotelManagementException
                   ("Número de días erroneo, menos de 1"))
        if numeroDias > 10:
            raise (hotelManagementException
                   ("Número de días erroneo, más de 10"))

        reservaHotel = hotelReservation(id_card, credit_card_number, arrival
                                        , name_surname, phone_number, room_type, num_days)
        localizador = reservaHotel.localizer
        self.guardar_reserva_en_archivo(localizador, id_card, credit_card_number
                                        , arrival, name_surname
                                        , phone_number, room_type, num_days)
        return localizador

    def guest_arrival(self, input_file):
        '''Función 2'''
        try:
            # Verificar si el archivo está vacío
            if os.stat(input_file).st_size == 0:
                raise hotelManagementException("El archivo de entrada está vacío")

            # Lee el archivo dado  y verificar que existe y está en formato JSON
            with open(input_file, 'r', encoding='utf-8') as f:
                datosReservaf2 = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("No se encuentra el archivo json") from e
        except json.JSONDecodeError as e:
            raise (hotelManagementException
                   ("El archivo de reservasf2 no está en formato JSON")) from e

        # Verificar si hay datos entre las llaves
        if not datosReservaf2:
            raise (hotelManagementException
                   ("El archivo de reservasf2 JSON está vacío"
                    " (no hay datos entre las llaves)"))

        # Verificar si hay una clave vacía en el JSON
        if "" in datosReservaf2:
            raise (hotelManagementException
                   ("Error, el JSON contiene una clave vacía"))

        # Verificar si hay una clave vacía en el JSON
        for key, value in datosReservaf2.items():
            if not value and key == ("Localizer"):
                raise (hotelManagementException
                       ("Error, el valor asociado a la clave Localizer está vacío"))
            if not value and key == ("IdCard"):
                raise (hotelManagementException
                       ("Error, el valor asociado a la clave IdCard está vacío"))

        # Verificar si el JSON tiene el Localizer y el IdCard
        if "Localizer" not in datosReservaf2 or "IdCard" not in datosReservaf2:
            raise (hotelManagementException
                   ("El archivo reservasf2 tiene un fallo"
                    " de escritura en alguna de las claves"))

        # Verificar si el valor de las claves está correctamente escrito
        if len(datosReservaf2["Localizer"]) > 32:
            raise (hotelManagementException
                   ("Localizer contiene más de 32 caracteres"))
        if len(datosReservaf2["Localizer"]) < 32:
            raise (hotelManagementException
                   ("Localizer contiene menos de 32 caracteres"))
        if not datosReservaf2["Localizer"].isalnum():
            raise (hotelManagementException
                   ("Localizer no contiene solo números o solo letras"))

        # Verificar que el IdCard tiene 8 números y 1 letra
        if len(datosReservaf2["IdCard"]) > 9:
            raise (hotelManagementException
                   ("IdCard contiene más de 9 caracteres"))
        if len(datosReservaf2["IdCard"]) < 9:
            raise (hotelManagementException
                   ("IdCard contiene menos de 9 caracteres"))
        if not nif.is_valid(datosReservaf2["IdCard"]):
            raise (hotelManagementException
                   ("El formato de IdCard no cumple el formato 8 dígitos y 1 letra"))

        localizer = datosReservaf2["Localizer"]
        idCard = datosReservaf2["IdCard"]

        # verificar que el localizador fue almacenado en el fichero de reservas y
        # que el localizador coincide con los datos que estaban en el fichero
        try:
            with open(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri"
                      r"\EG2\src\main\python\json_files\reservas.json"
                      , 'r', encoding='utf-8') as f:
                datosReservaf1 = json.load(f)
        except FileNotFoundError:
            datosReservaf1 = {}

        existe = 0
        posicion, contador = 0, 0
        for a in datosReservaf1:
            if a["Localizer"] == localizer:
                existe = 1
                posicion = contador
            contador += 1

        if existe == 0:
            raise (hotelManagementException
                   ("Error, el localizer del archivo no"
                    " coincide con ninguno de reservas"))

        reserva2 = datosReservaf1[posicion]
        localizer2 = reserva2["Localizer"]
        idCard2 = reserva2["IdCard"]
        arrivalReserva = reserva2["Arrival"]
        # arrivalReserva_datetime = datetime.strptime(arrivalReserva, "%d/%m/%Y")
        numDays = reserva2["NumDays"]
        roomType = reserva2["RoomType"]

        if localizer != localizer2:
            raise (hotelManagementException
                   ("El localizador de reservaf2 no se corresponde con "
                    "el localizador en el archivo de reservaf1"))

        if idCard != idCard2:
            raise (hotelManagementException
                   ("El DNI de reservaf2 no corresponde con el DNI de reservaf1"))

        hotel = hotelStay(idCard2, localizer2, numDays, roomType)
        arrival = hotel.arrival
        departure = hotel.departure
        roomKey = hotel.room_key
        dd, mm, yyyy = map(int, arrivalReserva.split('/'))
        if dd != arrival.day or mm != arrival.month or yyyy != arrival.year:
            raise (hotelManagementException
                   ("La fecha de llegada de reservaf2 no "
                    "coincide con la fecha de llegada en reservaf1"))
        (self.guardar_reserva2_en_archivo
         (localizer2, idCard2, roomType, arrival, departure, roomKey))
        return roomKey

    def guest_checkout(self, room_key):
        '''Función 3'''
        # comprobar q roomKey sea hexadecimal de 64 caracteres
        if len(room_key) < 64:
            raise hotelManagementException("roomKey tiene menos de 64 caracteres")
        if len(room_key) > 64:
            raise hotelManagementException("roomKey tiene más de 64 caracteres")
        if not re.match("^[a-fA-F0-9]{64}$", room_key):
            raise hotelManagementException("roomKey no es hexadecimal de 64 caracteres")
        nombreArchivo = (r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri"
                         r"\EG2\src\main\python\json_files\reservas2.json")
        datosReservaf1 = self.readdatafrom_json(nombreArchivo)

        if not datosReservaf1:
            raise hotelManagementException("El archivo de reservas2.json está vacío")

        hoy = datetime.now().date().strftime("%Y-%m-%d")
        existe = 0
        fechaSalida = ""
        # posicion, contador = 0, 0
        if not isinstance(datosReservaf1, list):
            datosReservaf1 = [datosReservaf1]
        for a in datosReservaf1:
            if a["roomKey"] == room_key:
                existe = 1
                if a["Departure"] != hoy:
                    raise hotelManagementException("La fecha de salida no es hoy")
                fechaSalida = a["Departure"]

        if existe == 0:
            raise hotelManagementException("No existe ninguna roomKey igual a la dada")

        self.insertar_datos(fechaSalida, room_key)
        return True
