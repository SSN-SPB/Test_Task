import unittest
from py_oop_02inheritance import BaseClass, LoginTest, BuyTest

class TestBaseClass(unittest.TestCase):

    def setup_method_invokes_correct_message(self):
        base = BaseClass()
        with self.assertLogs() as log:
            base.setup()
        self.assertIn("make setup base", log.output[0])

class TestLoginTest(unittest.TestCase):

    def setup_overrides_base_class(self):
        login_test = LoginTest()
        with self.assertLogs() as log:
            login_test.setup()
        self.assertIn("make setup login and override the base class", log.output[0])

    def run_invokes_correct_message(self):
        login_test = LoginTest()
        with self.assertLogs() as log:
            login_test.run()
        self.assertIn("make run login", log.output[0])

class TestBuyTest(unittest.TestCase):

    def setup_invokes_base_class_message(self):
        buy_test = BuyTest()
        with self.assertLogs() as log:
            buy_test.setup()
        self.assertIn("make setup base", log.output[0])

    def run_invokes_correct_message(self):
        buy_test = BuyTest()
        with self.assertLogs() as log:
            buy_test.run()
        self.assertIn("make run buy", log.output[0])

if __name__ == "__main__":
    unittest.main()
