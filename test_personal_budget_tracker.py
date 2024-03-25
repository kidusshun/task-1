import unittest
from unittest.mock import patch
from personal_budget_tracker import *

class TestCalc(unittest.TestCase):

    def get_last_balance(self):
        with open('database.csv','r') as read_file:
            data = list(csv.reader(read_file))
            if len(data) == 1:
                return 0
            return data[-1][-1]

    @patch('builtins.print')
    def test_show_menu(self,mock_print):

        expected_output = [
            "1. Grocery",
            "2. Rent",
            "3. Transportation",
            "4. Entertainment",
            "5. Deposit"
        ]
        show_menu()
        mock_print.assert_has_calls([unittest.mock.call(line) for line in expected_output])
    
    
    @patch('builtins.input', side_effect=['1'])
    def test_type_of_transaction_grocery(self, mock_input):
        result = type_of_transaction()
        self.assertEqual(result, "Grocery")



    @patch('builtins.input', side_effect=['2'])
    def test_type_of_transaction_rent(self,mock_input):
        result = type_of_transaction()
        self.assertEqual(result,"Rent")

    @patch('builtins.input', side_effect=['3'])
    def test_type_of_transaction_transportation(self,mock_input):
        result = type_of_transaction()
        self.assertEqual(result,"Transportation")


    @patch('builtins.input', side_effect=['4'])
    def test_type_of_transaction_entertainment(self,mock_input):
        result = type_of_transaction()
        self.assertEqual(result,"Entertainment")
    
    @patch('builtins.input', side_effect=['5'])
    def test_type_of_transaction_deposit(self,mock_input):
        result = type_of_transaction()
        self.assertEqual(result,"Deposit")
    

    def test_last_balance(self):
        last_val = self.get_last_balance()
        
        self.assertEqual(last_val,last_balance())

if __name__ == "__main__":
    unittest.main()