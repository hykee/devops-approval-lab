import unittest
from hello import message

class TestMessage(unittest.TestCase):
    def test_message(self):
        self.assertEqual(message(), "Version 2")

if __name__ == "__main__":
    unittest.main()