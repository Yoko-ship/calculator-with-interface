from calculator_project import calculator,get_entry
from unittest import TestCase,main

class Test_Calculator(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("5 + 3"),8)

    def test_minus(self):
        self.assertEqual(calculator("5 - 3"),2)

    def test_divide(self):
        self.assertEqual(calculator("6/2"),3)

    def test_multiply(self):
        self.assertEqual(calculator("6 * 2"),12)

    def no_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator("test")

        self.assertEqual("Выражение должно хотя - бы содержать 1 знак +-/*",e.exception.args[0])
        






if __name__ == "__main__":
    main()

