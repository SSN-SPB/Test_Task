import unittest
from unittest.mock import patch
from app import BaseClass, LoginTest, BuyTest


class TestBaseClass(unittest.TestCase):

    @patch("builtins.print")
    def test_baseclass_setup_prints_expected_output(self, mock_print):
        obj = BaseClass()
        obj.setup()

        mock_print.assert_any_call(f"from BaseClass setup {obj}")
        mock_print.assert_any_call("make setup base2")


class TestLoginTest(unittest.TestCase):

    @patch("builtins.print")
    def test_login_test_init_prints_activation(self, mock_print):
        lt = LoginTest()
        mock_print.assert_any_call("activate LoginTest")

    @patch("builtins.print")
    def test_login_test_setup_overrides_base(self, mock_print):
        lt = LoginTest()
        lt.setup()

        # First print contains dynamic dir(self), so we only check part of it
        self.assertIn("from LoginTest setup", mock_print.call_args_list[1][0][0])
        mock_print.assert_any_call("make setup login and override the base class")

    @patch("builtins.print")
    def test_login_test_run(self, mock_print):
        lt = LoginTest()
        lt.run()

        mock_print.assert_any_call("make run login")


class TestBuyTest(unittest.TestCase):

    @patch("builtins.print")
    def test_buy_test_init_prints_activation(self, mock_print):
        bt = BuyTest()
        mock_print.assert_any_call("activate BuyTest")

    @patch("builtins.print")
    def test_buy_test_inherits_base_setup(self, mock_print):
        bt = BuyTest()
        bt.setup()

        mock_print.assert_any_call(f"from BaseClass setup {bt}")
        mock_print.assert_any_call("make setup base2")

    @patch("builtins.print")
    def test_buy_test_run(self, mock_print):
        bt = BuyTest()
        bt.run()

        mock_print.assert_any_call("make run buy")


if __name__ == "__main__":
    unittest.main()