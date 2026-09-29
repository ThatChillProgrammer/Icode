import os
from services import coder

dir_path = os.getcwd() + '/'

#with open(dir_path + 'test.py') as filepath:
    #content = filepath.read().encode('UTF8')

def main():
    #with open(dir_path + "check.py", 'wb') as filepath:
    #    string1 = b"import unittest\n\n# The code you want to test (usually imported from another file)\ndef add_numbers(a, b):\n    return a + b\n\n# The test case class inheriting from unittest.TestCase\nclass TestMathOperations(unittest.TestCase):\n    \n    def test_add_success(self):\n        self.assertEqual(add_numbers(3, 5), 8)\n\n    def test_add_failure(self):\n        # This will fail intentionally to show you how a failure looks\n        self.assertEqual(add_numbers(1, 1), 5)\n\nif __name__ == '__main__':\n    unittest.main()\n"
    #    filepath.write(string1)


    agent = coder.Coder()
    agent.getModel()

    agent.init("Calculator", dir_path, "A calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division using python.")

    return 0


if __name__ == "__main__":
    main()
