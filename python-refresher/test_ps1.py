import unittest
from ps1 import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        temp = BankAccount(100, "Zack Zhang", 123456)
        self.assertEqual(temp.deposit(10), 110)
        self.assertEqual(temp.deposit(-1), -1)
        self.assertNotEqual(temp.deposit("10"), 120)
        self.assertNotEqual(temp.deposit(-5), 105)
        self.assertEqual(temp.deposit(5.75), 115.75)

    def test_withdraw(self):
        temp = BankAccount(1000, "Eric Zhang", 654321)
        self.assertEqual(temp.withdraw(100), 900)
        self.assertNotEqual(temp.withdraw(-50), 950)
        self.assertEqual(temp.withdraw("cat"), -1)
        self.assertEqual(temp.withdraw(100.5), 799.5)
        self.assertNotEqual(temp.withdraw(50), 750)
        self.assertEqual(temp.withdraw(10000), -1)


if __name__ == "__main__":
    unittest.main()
