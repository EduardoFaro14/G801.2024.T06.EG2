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
            if index + 1 in [1, 62, 63]:
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
                            41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]:
                testId = "TC" + string(index + 1)
                with self.subTest(testId):
                    print("Ejecutando: " + testId + ": " + inputData)
                    self.generate_tmp_test_data_file(inputData)
                    hm = hotelManager()
                    with self.assertRaises(hotelManagementException) as result:
                        roomKey = hm.guest_arrival(self.__path_tests + self.__tmp_test_data_file)
                    match testId:
                        case "TC2":
                            self.assertEqual(roomKey, "3ff517743faae67b33ddefa77163")

    def generate_tmp_test_data_file(self, inputData):
        nombreArchivo = self.__tmp_test_data_file

        if os.path.isfile(nombreArchivo):
            # Si existe, vacía el archivo
            open(nombreArchivo, 'w').close()

        with open(nombreArchivo, 'w', encoding='utf-8') as f:
            json.dump(inputData, f, ensure_ascii=False, indent=4)