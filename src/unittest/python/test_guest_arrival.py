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

    __path_tests =
    __path_data =

    @classmethod
    def setUpClass(cls):
        try:
            with open(cls.__path_tests + r"\f2_tests.json", encoding="UTF-8", mode="r") as f:
                testf2_data = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Archivo de prueba incorrecto o ruta de archivo incorrecta") from e
        except json.JSONDecodeError:
            testf2_data = {}

        cls.__test_data = testf2_data
        json_files_path = cls.__path_tests
        # Path del archivo de reservas para borrarlo si existe
        file_store = json_files_path + r"\reservas.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


    def test_guest_arrival_tests_valid(self): #TEST VALIDO
        for index, input_data in enumerate(self.__testf2_data):
            if index + 1 in [1, 15]:
                test_id = "TC" + string(index + 1)
                with self.subTest(test_id):
                    print("Ejecutando: " + test_id + ": " + input_data)
                    self.generate_tmp_test_data_file(input_data)
                    hm = HotelManager()
                    room_key = hm.guest_arrival(self.__path_tests + self.__tmp_test_data_file)
                    match test_id:
                        case "TC1":
                            self.assertEqual(room_key, 3ff517743faae67b33ddefa77163")