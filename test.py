import unittest
from pdu_convertor import text_to_pdu


class TestConverter(unittest.TestCase):

    def setUp(self):
        pass

    def test_str_to_pdu(self):
        self.assertEqual(text_to_pdu('*124#'), 'AA988C3602')


if __name__ == '__main__':
    unittest.main()
