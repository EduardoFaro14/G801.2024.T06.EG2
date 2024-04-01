import hashlib
import json
import unittest
import os.path
from unittest import TestCase

from tomlkit import string

from src.main.python.uc3m_travel.hotel_manager import hotelManager
from src.main.python.uc3m_travel.hotel_management_exception import hotelManagementException
from src.main.python.uc3m_travel.hotel_stay import hotelStay
from pathlib import Path
from datetime import datetime
from freezegun import freeze_time


class testGuestArrival(TestCase):
    __path_tests = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __path_data = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __tmp_test_data_file = str(r"reservas2.json")

    @classmethod
    def setUpClass(cls):

        jsonFilesPath = cls.__path_tests
        # Path del archivo de reservas para borrarlo si existe
        fileStore = jsonFilesPath + r"\reservas2.json"
        if os.path.isfile(fileStore):
            os.remove(fileStore)

    def get_hash(self):
        try:
            with open(self.__path_tests + r"\reservas.json", encoding='UTF-8', mode="r") as f:
                file_hash = hashlib.md5(f.__str__().encode()).hexdigest()
        except FileNotFoundError:
            file_hash = ""
        return file_hash

    @freeze_time("2024-06-14")
    def test_guest_arrival_tests_tc1(self):  # TEST VALIDO
        index = 0
        hash1 = self.get_hash()
        if index + 1 in [1]:
            testId = "TC" + str(index + 1)
            with self.subTest(testId):
                inputData = self.__path_tests + r"\test2\test" + str(index + 1) + r".json"
                print("Ejecutando: " + testId)
                # self.generate_tmp_test_data_file(inputData)
                hm = hotelManager()
                roomKey = hm.guest_arrival(inputData)
                match testId:
                    case "TC1":
                        self.assertEqual(roomKey, "fbf2c46543aa1573cea3a28be76f1f8bf8f4a8267146133e0cd1a81e6864cd53")
        hash2 = self.get_hash()
        if hash2 != hash1:
            raise hotelManagementException("El archivo de reservas ha sido modificado")

    @freeze_time("2024-06-24")
    def test_guest_arrival_tests_tc2(self):  # TEST INVALIDO
        hash1 = self.get_hash()
        for index in range(72):

            if index + 1 in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                             41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
                             62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                testId = "TC" + str(index + 1)
                inputData = self.__path_tests + r"\test2\test" + str(index + 1) + r".json"
                with (self.subTest(testId)):
                    print("Ejecutando: " + testId)
                    # self.generate_tmp_test_data_file(inputData)
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        roomKey = hm.guest_arrival(inputData)
                    print(testId)
                    match str(testId):
                        case "TC2":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "El archivo de entrada está vacío")
                        case "TC3":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC5":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC6":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC7":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC8":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC9":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC10":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC11":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC12":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC13":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC14":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC15":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC17":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC18":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC20":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC21":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC23":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC24":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC26":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "T27":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC28":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC29":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC30":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC31":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC32":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC33":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC34":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC35":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC36":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC37":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC38":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC39":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC40":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC42":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")

                        case "TC43":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC45":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC46":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC48":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC49":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC51":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC52":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC53":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC54":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC55":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC56":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC57":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC59":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC60":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC63":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC64":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC66":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC67":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")
                        case "TC71":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 no está en formato JSON")

                        case "TC4":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo de reservasf2 JSON está vacío (no hay datos entre las llaves)")
                        case "TC16":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "Error, el JSON contiene una clave vacía")
                        case "TC22":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "Error, el JSON contiene una clave vacía")
                        case "TC19":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "Error, el valor asociado a la clave Localizer está vacío")
                        case "TC25":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "Error, el valor asociado a la clave IdCard está vacío")
                        case "TC41":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo reservasf2 tiene un fallo de escritura en alguna de las claves")

                        case "TC47":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo reservasf2 tiene un fallo de escritura en alguna de las claves")
                        case "TC58":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo reservasf2 tiene un fallo de escritura en alguna de las claves")
                        case "TC65":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El archivo reservasf2 tiene un fallo de escritura en alguna de las claves")

                        case "TC44":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "Localizer contiene más de 32 caracteres")
                        case "TC50":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "IdCard contiene más de 9 caracteres")
                        case "TC61":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "Localizer contiene menos de 32 caracteres")
                        case "TC68":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message, "IdCard contiene menos de 9 caracteres")
                        case "TC62":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "Localizer no contiene solo números o solo letras")
                        case "TC69":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El formato de IdCard no cumple el formato 8 dígitos y 1 letra")
                        case "TC70":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "El formato de IdCard no cumple el formato 8 dígitos y 1 letra")
                        case "TC72":
                            print(result.exception.message)
                            self.assertEqual(result.exception.message,
                                             "La fecha de llegada de reservaf2 no coincide con la fecha de llegada en reservaf1")
        hash2 = self.get_hash()
        if hash2 != hash1:
            raise hotelManagementException("El archivo de reservas ha sido modificado")

    # no hace falta porque hemos hecho manualmente lo de pasar los tests a ficheros json individuales
    '''def generate_tmp_test_data_file(self, inputData):
        nombreArchivo = self.__path_tests + self.__tmp_test_data_file

        if os.path.isfile(nombreArchivo):
            # Si existe, vacía el archivo
            open(nombreArchivo, 'w').close()

        with open(nombreArchivo, 'w', encoding='utf-8') as f:
            json.dump(inputData, f, ensure_ascii=False, indent=4)'''
