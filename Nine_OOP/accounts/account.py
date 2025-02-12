from Nine_OOP.accounts.negative_amount_exception import NegativeAmountException

class Account:
    """
    This class represents a simple bank account
    """
    #method is just a function that belongs to a class
    def __init__(self, initial_amount, firstname, lastname):
        """
        __init__ is a CONSTRUCTOR
        It is called when we create objects from this class
        """
        self._balance = initial_amount # semi-private
        self.first_name = firstname #public, no underscore
        self.__last_name = lastname # private
        self._account_holder_name = firstname + " " + lastname

# getters and setters JAVA
# properties c#
# getters are used to READ a piece of data: translation or formatting
# setters are used when we WRITE/CHANGE a piece of data

    def get_lastname(self):
        return self.__last_name.title()

    def set_lastname(self, new_lastname):
            #do validation
        self.__last_name = new_lastname

    # property syntax approach
    # @property is a DECORATOR
    # means - I am a getter
    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, name):
        self._account_holder_name = name
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.__last_name = name_parts[1]

    def get_balance(self):
        return f"${self._balance}"

# overriding
# we are overriding an inherited method
    def __str__(self):
        return f"Account:\nFirstname: {self.first_name}\nLastname: {self.get_lastname()}\n" \
                f"Balance: {self._balance}\n******************************"

    def deposit(self, deposit_amount):
        if deposit_amount <0:
            raise NegativeAmountException('Amount can not be negative')
        self._balance += deposit_amount