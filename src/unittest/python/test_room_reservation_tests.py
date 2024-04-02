'''Test_room_reservation_test'''
from unittest import TestCase
import json
import os.path
from uc3m_travel.hotel_manager import hotelManager
from uc3m_travel.hotel_management_exception import hotelManagementException


class TestRoomResevation(TestCase):
    '''Clase de tests'''

    __path_tests = (str
                    (r"C:\Users\eduardo faro jr\OneDrive\Documentos"
                     r"\3 curso 2 cuatri\EG2\src\main\python\json_files"))
    __path_data = (str
                   (r"C:\Users\eduardo faro jr\OneDrive\Documentos"
                    r"\3 curso 2 cuatri\EG2\src\main\python\json_files"))
    @classmethod
    def setUpClass(cls):
        try:
            with open(cls.__path_tests + r"\test1.json"
                    , encoding="UTF-8", mode="r") as f:
                testDataCreditCard = json.load(f)
        except FileNotFoundError as e:
            raise (hotelManagementException
                   ("Wrong file or file path")) from e
        except json.JSONDecodeError:
            testDataCreditCard = []
        cls.__test_data_credit_card = testDataCreditCard
        jsonFilesPath = cls.__path_tests
        fileStore = jsonFilesPath + r"\reservas.json"
        if os.path.isfile(fileStore):
            os.remove(fileStore)

    def test_credit_card_number_tc1(self):
        '''Test OK (válidos)'''
        for inputData in self.__test_data_credit_card:
            if (inputData["idTest"] == "TC1"
                    or inputData["idTest"] == "TC2"
                    or inputData["idTest"] == "TC3"):
                with self.subTest(inputData["idTest"]):
                    print("Executing: " + inputData["idTest"])
                    hm = hotelManager()
                localizer = (hm.room_reservation
                             (inputData["CreditCard"],inputData["IdCard"]
                              , inputData["NameSurname"], inputData["phoneNumber"]
                              , inputData["RoomType"], inputData["Arrival"]
                              , inputData["NumDays"]))
                match inputData["idTest"]:
                    case "TC1":
                        (self.assertEqual
                         (localizer, "43d9d717214b9f6858bd2b55be901645"))
                    case "TC2":
                        (self.assertEqual
                         (localizer, "ec4a527e598a64d8dcf38b9d68b4da9e"))
                    case "TC3":
                        (self.assertEqual
                         (localizer, "19102761a0e960cb8cb97d39a71533e5"))

    def test_credit_card_number_tc2(self):
        """ TestCase: TC2 - Expected KO. Checks Card Number is K0"""
        for inputData in self.__test_data_credit_card:
            if inputData["idTest"] not in ["TC1","TC2","TC3"]:
                with self.subTest(inputData["idTest"]):
                    print("Executing: " + inputData["idTest"])
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        hm.room_reservation(inputData["CreditCard"],
                                            inputData["IdCard"],
                                            inputData["NameSurname"],
                                            inputData["phoneNumber"],
                                            inputData["RoomType"],
                                            inputData["Arrival"],
                                            inputData["NumDays"])
                    match inputData["idTest"]:
                        case "TC4":
                            self.assertEqual(result.exception.message
                                             , "Número de tarjeta de crédito "
                                               "erroneo, algoritmo de luhn")
                        case "TC5":
                            self.assertEqual(result.exception.message,
                                             "Número de tarjeta de"
                                             " crédito erroneo, tipo de dato")
                        case "TC6":
                            self.assertEqual(result.exception.message,
                                             "Número de tarjeta de crédito erroneo"
                                             ", más de 16 dígitos")
                        case "TC7":
                            self.assertEqual(result.exception.message,
                                             "Número de tarjeta de crédito erroneo,"
                                             " menos de 16 dígitos")
                        case "TC8":
                            self.assertEqual(result.exception.message,
                                             "Número de DNI erroneo, algoritmo de nift")
                        case "TC9":
                            self.assertEqual(result.exception.message,
                                             "Número de DNI erroneo, más de 9 caracteres")
                        case "TC10":
                            self.assertEqual(result.exception.message,
                                             "Número de DNI erroneo, menos de 9 caracteres")
                        case "TC11":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo, tipo de dato")
                        case "TC12":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo, no hay espacios")
                        case "TC13":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo,"
                                             " más de 50 caracteres")
                        case "TC14":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo,"
                                             " menos de 10 caracteres")
                        case "TC15":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo,"
                                             " dos espacios seguidos")
                        case "TC16":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo,"
                                             " primer caracter es un espacio")
                        case "TC17":
                            self.assertEqual(result.exception.message,
                                             "Nombre y apellido erroneo,"
                                             " último caracter es un espacio")
                        case "TC18":
                            self.assertEqual(result.exception.message,
                                             "Número de teléfono erroneo, tipo de dato")
                        case "TC19":
                            self.assertEqual(result.exception.message,
                                             "Número de teléfono erroneo, más de 9 dígitos")
                        case "TC20":
                            self.assertEqual(result.exception.message,
                                             "Número de teléfono erroneo,"
                                             " menos de 9 dígitos")
                        case "TC21":
                            self.assertEqual(result.exception.message,
                                             "Tipo de habitación erronea,"
                                             " no es ni single ni double ni suite")
                        case "TC22":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea,"
                                             " más de 31 días en un mes de 31")
                        case "TC23":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea, menos de día 1")
                        case "TC24":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea,"
                                             " más de 30 días en un mes de 30")
                        case "TC25":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea,"
                                             " más de 28 días en febrero no bisiesto")
                        case "TC26":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea,"
                                             " más de 29 días en febrero bisiesto")
                        case "TC27":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea, tipo de dato")
                        case "TC28":
                            self.assertEqual(result.exception.message,
                                             "Fecha de llegada erronea,"
                                             " fecha anterior a la actual")
                        case "TC29":
                            self.assertEqual(result.exception.message,
                                             "Número de días erroneo, más de 10")
                        case "TC30":
                            self.assertEqual(result.exception.message,
                                             "Número de días erroneo, menos de 1")
                        case "TC31":
                            self.assertEqual(result.exception.message,
                                             "Número de días erroneo, tipo de dato")
                        case "TC32":
                            self.assertEqual(result.exception.message,
                                             "Número reserva erroneo,"
                                             " más de una reserva")
