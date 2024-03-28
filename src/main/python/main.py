"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS"""
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from src.main.python.uc3m_travel import hotelManager
from src.main.python.uc3m_travel.hotel_management_exception import hotelManagementException

def Main():
    """ descripción del main"""
    mng = hotelManager()
    res = mng.readdatafrom_json("test.json")
    strRes = str(res)
    print(strRes)
    print("CreditCard: " + res.credit_card)
    print(res.localizer)

    #credit_card_number = str(res.credit_card)
    credit_card_number = "5555555555554444"
    id_card = "12345678Z"
    name_surname = "John Doeghy"
    phone_number = "123456789"
    room_type = "SINGLE"
    arrival = "20/06/2024"
    num_days = 3

    try:
        reserva = mng.room_reservation(credit_card_number, id_card, name_surname, phone_number, room_type, arrival,
                                       num_days)
        print("Reserva realizada exitosamente. Número de reserva:", reserva)
    except hotelManagementException as e:
        print("Error al realizar la reserva:", str(e))


if __name__ == "__main__":
    Main()
