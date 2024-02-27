"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS"""
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from src.main.python.uc3m_travel import hotelManager


def Main():
    """ descripción del main"""
    mng = hotelManager()
    res = mng.readdatafrom_json("test.json")
    strRes = str(res)
    print(strRes)
    print("CreditCard: " + res.credit_card)
    print(res.localizer)

if __name__ == "__main__":
    Main()
