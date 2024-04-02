import copy
import json
import os.path
from unittest import TestCase

from freezegun import freeze_time
from src.main.python.uc3m_travel.hotel_manager import hotelManager
from src.main.python.uc3m_travel.hotel_management_exception import hotelManagementException


class testGuestCheckout(TestCase):

    __path_tests = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __path_data = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")

    @classmethod
    def setUpClass(cls):
        try:
            with open(cls.__path_tests + r"\test3.json", encoding="UTF-8", mode="r") as f:
                testDataCreditCard = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError:
            testDataCreditCard = []
        cls.__test_data_credit_card = testDataCreditCard
        jsonFilesPath = cls.__path_tests
        fileStore = jsonFilesPath + r"\reservas3.json"
        if os.path.isfile(fileStore):
            os.remove(fileStore)

    @freeze_time("2024-06-16")
    def test_guest_checkout_tc1(self):  # TEST VALIDO
        for inputData in self.__test_data_credit_card:
            if inputData["idTest"] == "TC1":
                with self.subTest(inputData["idTest"]):
                    print("Executing: " + inputData["idTest"])
                    hm = hotelManager()
                verdadero = hm.guest_checkout(inputData["roomKey"])
                match inputData["idTest"]:
                    case "TC1":
                        self.assertEqual(verdadero, True)



    @freeze_time("2024-06-16")
    def test_guest_checkout_tc2(self):  # TEST INVALIDOS
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC2", "TC3", "TC4", "TC5", "TC6"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    match input_data["idTest"]:
                        case "TC2":
                            self.assertEqual(result.exception.message,"roomKey tiene menos de 64 caracteres")
                        case "TC3":
                            self.assertEqual(result.exception.message, "roomKey tiene más de 64 caracteres")
                        case "TC4":
                            self.assertEqual(result.exception.message, "roomKey no es hexadecimal de 64 caracteres")
                        case "TC5":
                            self.assertEqual(result.exception.message, "No existe ninguna roomKey igual a la dada")
                        case "TC6":
                            self.assertEqual(result.exception.message, "Número de roomKey repetido")

    @freeze_time("2024-07-17")
    def test_guest_checkout_tc3(self):  # TEST INVALIDOS
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC7"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    match input_data["idTest"]:
                        case "TC7":
                            self.assertEqual(result.exception.message,"La fecha de salida no es hoy")

    def test_guest_checkout_tc4(self):  # TEST INVALIDO COMPROBAR JSONDECODEERROR EN RESERVAS2.JSON
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC8"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="r") as f:
                        data = json.load(f)
                    data = copy.deepcopy(data)
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="a") as f:
                        json.dump("hola", f)
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="w") as f:
                        json.dump(data, f)

                    match input_data["idTest"]:
                        case "TC8":
                            self.assertEqual(result.exception.message,"El archivo de reservasf2 no está en formato JSON")

    def test_guest_checkout_tc5(self):  # TEST INVALIDO COMPROBAR ARCHIVO RESERVAS2 VACIO
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC9"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="r") as f:
                        data = json.load(f)
                    data = copy.deepcopy(data)
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="w") as f:
                        json.dump("", f)
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    with open(self.__path_tests + r'\reservas2.json', encoding="UTF-8", mode="w") as f:
                        json.dump(data, f)

                    match input_data["idTest"]:
                        case "TC9":
                            self.assertEqual(result.exception.message,"El archivo de reservas2.json está vacío")

    @freeze_time("2024-06-16")
    def test_guest_checkout_tc6(self):  # TEST INVALIDO COMPROBAR ARCHIVO RESERVAS3 JSONDECODEERROR
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC10"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    with open(self.__path_tests + r'\reservas3.json', encoding="UTF-8", mode="r") as f:
                        data = json.load(f)
                    data = copy.deepcopy(data)
                    with open(self.__path_tests + r'\reservas3.json', encoding="UTF-8", mode="a") as f:
                        json.dump("hola", f)
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    with open(self.__path_tests + r'\reservas3.json', encoding="UTF-8", mode="w") as f:
                        json.dump(data, f)

                    match input_data["idTest"]:
                        case "TC10":
                            self.assertEqual(result.exception.message,"El archivo de reservas3 no está en formato JSON")

    @freeze_time("2024-06-16")
    def test_guest_checkout_tc7(self):  # TEST INVALIDO COMPROBAR ARCHIVO RESERVAS3 JSONDECODEERROR
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] in ["TC11"]:
                with self.subTest(input_data["idTest"]):
                    print("Executing: " + input_data["idTest"])
                    hm = hotelManager()
                    originalFilePath = r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files\reservas2.json"
                    newFilePath = r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files\reservas2_new.json"
                    os.rename(originalFilePath, newFilePath)
                    with self.assertRaises(hotelManagementException) as result:
                        hm.guest_checkout(input_data["roomKey"])
                    os.rename(newFilePath, originalFilePath)
                    match input_data["idTest"]:
                        case "TC11":
                            self.assertEqual(result.exception.message,
                                             "Wrong file or file path")


