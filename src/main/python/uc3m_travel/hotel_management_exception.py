"""Modulo hotelManagementException"""
class hotelManagementException(Exception):
    """gestión """
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """mensaje"""
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value
