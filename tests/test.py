import unittest
from PDUUSSDConverter.converter import text_to_pdu, pdu_to_text


class TestConverter(unittest.TestCase):

    def setUp(self):
        pass

    def test_str_to_pdu(self):
        self.assertEqual(text_to_pdu('*124#'), 'AA988C3602')

    def test_pdu_to_str(self):
        self.assertEqual(pdu_to_text('54747A0E6A97E7F3F0B90CBA87E7A0F1DB6D2FCBE9657208'), 'This message was converted!')


if __name__ == '__main__':
    unittest.main()
