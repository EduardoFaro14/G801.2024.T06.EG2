''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib

class hotelStay():
    """Gestión de estancia"""
    def __init__(self, idcard, localizer, numdays, room_type):
        self.__alg = "SHA-256"
        self.__type = room_type
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + self.__arrival + \
            ",departure:" + self.__departure + "}"

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


"""NUEVO QUE HE AÑADIDO TENGO QUE REVISARLO """
    def guest_arrival(input_file, stays_file):
        try:
            # Open input file and get data inside (check exists, check json format)
            with open(input_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            raise HotelManagementException("No se encuentra el archivo de datos")
        except json.JSONDecodeError:
            raise HotelManagementException("El archivo no tiene formato JSON")

        # Verificar si el JSON tiene la estructura esperada
        if "Localizer" not in data or "IdCard" not in data:
            raise HotelManagementException("El JSON no tiene la estructura esperada.")

        localizer = data["Localizer"]
        idcard = data["IdCard"]

        # Verificar si el localizador existe en el fichero de estancias
        try:
            with open(stays_file, 'r') as file:
                stays_data = json.load(file)
        except FileNotFoundError:
            stays_data = {}

        if localizer not in stays_data:
            raise HotelManagementException("El localizador no se corresponde con los datos almacenados.")

        # Obtener los datos de la estancia del localizador
        stay_data = stays_data[localizer]

        if idcard != stay_data["idcard"]:
            raise HotelManagementException("El DNI no se corresponde con los datos almacenados.")

        # Obtener la fecha de llegada esperada
        expected_arrival = stay_data["arrival"]

        # Verificar si la fecha de llegada coincide con la esperada
        if expected_arrival != data["arrival"]:
            raise HotelManagementException("La fecha de llegada no se corresponde con la fecha de reserva.")

        # Crear objeto HotelStay
        hotel_stay = HotelStay(idcard, localizer, 1, stay_data["typ"])

        # Guardar la estancia y la clave de la habitación en el fichero de estancias
        stays_data[localizer]["room_key"] = hotel_stay.room_key
        with open(stays_file, 'w') as file:
            json.dump(stays_data, file, indent=4)

        # Devolver la clave de la habitación
        return hotel_stay.room_key

    # Ejemplo de uso
    input_file = "datos_reserva.json"
    stays_file = "estancias.json"
    try:
        room_key = guest_arrival(input_file, stays_file)
        print("Clave de la habitación generada:", room_key)
    except HotelManagementException as e:
        print("Error:", e)
