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
def test_guest_arrival_tests_valid(self): #TEST VALIDO
    for index, input_data in enumerate(self.__test_data_f2):
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