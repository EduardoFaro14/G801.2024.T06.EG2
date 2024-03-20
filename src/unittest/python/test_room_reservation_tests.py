import json
import unittest
import os.path
from unittests import TestCase
from uc3m_travel.hotel_manager import hotelManager
from uc3m_travel.hotel_management_exception import hotelManagementException
from pathlib import Path
__ path_tests = str(Path.home()) + "/PycharmProjects/G89.2024.T00.GE2/src/data/tests/"
__ path_data = str(Path.home()) + "/PycharmProjects/G89.2024.T00.GE2/src/data/"

class testRoomResevation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        try:
            with open(self.__path_tests + "f1_test_credit_card_number.json", encoding="UTF-8", mode="r") as f:
                test_data_credit_card = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError:
            test_data_credit_card = []
        self.__test_data_credit_card = test_data_credit_card

    def test_credit_card_number_tc1(self):
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] == "TC1":
                hm = hotelManager()
                localizer = hm.room_reservation(input_data["creditCardNumber"],input_data["idCard"],
                                                input_data["nameSurname"], input_data["phoneNumber"],
                                                input_data["roomType"], input_data["arrival"],
                                                input_data["numDays"])
                self.assertEqual(localizer, "5555555555554444")

    def test_credit_card_number_tc2(self):
        """ TestCase: TC2 - Expected KO. Checks Card Number is K0"""
        for input_data in self.__test_data_credit_card:
            if input_data["idTest"] == "TC2":
                hm = hotelManager()
                with self.assertRaises(hotelManagementException) as result:
                    hm.room_reservation(input_data["creditCardNumber"], input_data["idCard"],
                                        input_data["nameSurname"], input_data["phoneNumber"],
                                        input_data["roomType"], input_data["arrival"],
                                        input_data["numDays"])
                    self.assertEqual(result.exception.message,"Invalid credit card number provided")

