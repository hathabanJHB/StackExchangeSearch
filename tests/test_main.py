from unittest import TestCase
import main

class TestMain(TestCase):

    def test_get_error_correct(self):
        msg  = main.get_error('python3 tests/testingFile.py')
        self.assertEqual(msg,"TypeError: unsupported operand type(s) for +: 'int' and 'str'") 
