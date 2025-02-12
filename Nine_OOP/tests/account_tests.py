import unittest
from Nine_OOP.accounts.account import Account
from Nine_OOP.accounts.negative_amount_exception import NegativeAmountException

# this is inheritance
# inheritance represents an "is kind of" relationship
class TestAccount(unittest.TestCase):

    #TDD cycle
    #RED -> GREEN -> REFACTOR
    #TEST FAILS, TEST PASSES, TIDY UP

    def test_deposit_ten_dollars(self):
        # TRIPLE 'A' pattern
        # Arrange, Act, Assert
        # Arrange
        test_account = Account(0, 'Julie', 'Dooley')
        amount = 10
        final_balance = 10

        # Act
        test_account.deposit(amount)

        # Assert
        self.assertEqual(final_balance, int(test_account.get_balance()[1:]))

    def test_deposit_five_dollars(self):
        test_account = Account(0, 'Julie', 'Dooley')
        amount = 5
        final_balance = 5

        # Act
        test_account.deposit(amount)

        # Assert
        self.assertEqual(final_balance, int(test_account.get_balance()[1:]))

    def test_negative_deposit_amount_raises_exception(self):
        # Arrange
        test_account = Account(500, 'Julie', 'Dooley')
        amount = -50
        final_balance = 500
        with self.assertRaises(NegativeAmountException) as context:
            test_account.deposit(amount)
        self.assertTrue('Amount can non be negative', context.exception)
