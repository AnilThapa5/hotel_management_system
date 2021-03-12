import unittest
import os



class Test_Customer(unittest.TestCase):

    def test_fullname(self):
        cust =customer('susmita','devkota')
        self.assertEqual(cust, "susmita devkota")



   

if __name__ == '__main__':
    unittest.main()