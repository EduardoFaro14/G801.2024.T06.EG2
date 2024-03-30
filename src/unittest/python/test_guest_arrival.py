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

class testGuestArrival(TestCase):

    __path_tests = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __path_data = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __tmp_test_data_file = str(r"test_reservas2.json")

    @classmethod
    def setUpClass(cls):
        try:
            with open(cls.__path_tests + r"\test2.json", encoding="UTF-8", mode="r") as f:
                testf2Data = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Archivo de prueba incorrecto o ruta de archivo incorrecta") from e
        except json.JSONDecodeError:
            testf2Data = {}

        cls.__testf2_data = testf2Data
        jsonFilesPath = cls.__path_tests
        # Path del archivo de reservas para borrarlo si existe
        fileStore = jsonFilesPath + r"\reservas2.json"
        if os.path.isfile(fileStore):
            os.remove(fileStore)


    def test_guest_arrival_tests_tc1(self): #TEST VALIDO
        for index, inputData in enumerate(self.__testf2_data):
            if index + 1 in [1]:
                testId = "TC" + str(index + 1)
                with self.subTest(testId):
                    print("Ejecutando: " + testId + ": " + inputData)
                    self.generate_tmp_test_data_file(inputData)
                    hm = hotelManager()
                    roomKey = hm.guest_arrival(self.__path_tests + self.__tmp_test_data_file)
                    match testId:
                        case "TC1":
                            self.assertEqual(roomKey, "3ff517743faae67b33ddefa77163")

    def test_guest_arrival_tests_tc2(self): #TEST INVALIDO
        for index, inputData in enumerate(self.__testf2_data):
            if index + 1 in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                            21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                            41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,
                             62, 63, 64, 65, 66, 67, 68, 69, 70]:
                testId = "TC" + string(index + 1)
                with ((self.subTest(testId))):
                    print("Ejecutando: " + testId + ": " + inputData)
                    self.generate_tmp_test_data_file(inputData)
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        roomKey = hm.guest_arrival(self.__path_tests + self.__tmp_test_data_file)
                    match testId:
                        case "TC2":
                            self.assertEqual(result.exception.message, "El archivo de entrada está vacío")
                        case "TC3", "TC5", "TC6", "TC7", "TC8", "TC9", "TC10", "TC11", "TC12", "TC13", "TC14", "TC15", "TC17", "TC18",
                            "TC20", "TC21", "TC23", "TC24", "TC26", "TC28", "TC29", "TC30", "TC31", "TC32", "TC33", "TC34", "TC35",
                            "TC36", "TC37", "TC38", "TC39", "TC40", "TC42", "TC43", "TC45", "TC46", "TC48", "TC49", "TC51", "TC52",
                            "TC53", "TC54", "TC55", "TC56", "TC57", "TC59", "TC60", "TC63", "TC64", "TC66", "TC67", "TC71":
                            self.assertEqual(result.exception.message, "El archivo de reservasf2 no está en formato JSON")
                        case "TC4":
                            self.assertEqual(result.exception.message, "El archivo de reservasf2 JSON está vacío (no hay datos entre las llaves)")
                        case "TC16", "TC22":
                            self.assertEqual(result.exception.message, "Error, el JSON contiene una clave vacía")
                        case "TC19":
                            self.assertEqual(result.exception.message, "Error, el valor asociado a la clave Localizer está vacío")
                        case "TC25":
                            self.assertEqual(result.exception.message,
                                             "Error, el valor asociado a la clave IdCard está vacío")
                        case "TC27":
                            self.assertEqual(result.exception.message, "El archivo de reservasf2 JSON contiene más de un diccionario")
                        case "TC41", "TC47", "TC58", "TC65":
                            self.assertEqual(result.exception.message, "El archivo reservasf2 tiene un fallo de escritura en alguna de las claves")
                        case "TC44", "TC50", "TC61", "TC68":
                            self.assertEqual(result.exception.message, "Las claves no contienen un formato válido")
                        case "TC62", "TC70":
                            self.assertEqual(result.exception.message, "Los datos de las claves tienen caracteres que no son letras o números")
                        case "TC69":
                            self.assertEqual(result.exception.message, "El formato de IdCard no cumple el formato 8 dígitos y 1 letra")

    def generate_tmp_test_data_file(self, inputData):
        nombreArchivo = self.__tmp_test_data_file

        if os.path.isfile(nombreArchivo):
            # Si existe, vacía el archivo
            open(nombreArchivo, 'w').close()

        with open(nombreArchivo, 'w', encoding='utf-8') as f:
            json.dump(inputData, f, ensure_ascii=False, indent=4)