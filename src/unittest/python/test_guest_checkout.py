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


class testGuestCheckout(TestCase):

    __path_tests = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")
    __path_data = str(r"C:\Users\eduardo faro jr\OneDrive\Documentos\3 curso 2 cuatri\EG2\src\main\python\json_files")

    @classmethod
    def setUpClass(cls):
        try:
            with open(cls.__path_tests + r"\test1.json", encoding="UTF-8", mode="r") as f:
                test_data_credit_card = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError:
            test_data_credit_card = []
        cls.__test_data_credit_card = test_data_credit_card
        JSON_FILES_PATH = cls.__path_tests
        file_store = JSON_FILES_PATH + r"\reservas.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


    def test_guest_checkoutok(self):  # TEST VALIDO
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

        hash2 = self.get_hash()
        if hash2 != hash1:
            raise hotelManagementException("El archivo de reservas ha sido modificado")


    def test_guest_checkoutko(self):  # TEST INVALIDOS

        hash1 = self.get_hash()
        for index in range(72):

            if index + 1 in [2, 3, 4]:
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
