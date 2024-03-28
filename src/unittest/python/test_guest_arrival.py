import json
import unittest
import os.path
from unittest import TestCase
from uc3m_travel.hotel_manager import hotelManager
from uc3m_travel.hotel_management_exception import hotelManagementException
from uc3m_travel.hotel_stay import hotelStay
from pathlib import Path
from datetime import datetime

class testGuestArrival(TestCase):

    __path_tests = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __path_data = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")

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


    def test_guest_arrival_tests_valid(self): #TEST VALIDO
        for index, input_data in enumerate(self.__testf2_data):
            if index + 1 in [1, 62, 63]:
                test_id = "TC" + string(index + 1)
                with self.subTest(test_id):
                    print("Ejecutando: " + test_id + ": " + input_data)
                    self.generate_tmp_test_data_file(input_data)
                    hm = hotelManager()
                    roomKey = hm.guest_arrival(self.__path_tests + self.__tmp_test_data_file)
                    match test_id:
                        case "TC1":
                            self.assertEqual(roomKey, "3ff517743faae67b33ddefa77163")