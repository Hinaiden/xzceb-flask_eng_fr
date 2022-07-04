import unittest
import translator

class TestFr2EnMethod(unittest.TestCase):
    def test_translateBonjour(self):
        frenchText = 'Bonjour'
        transatedText = translator.french_to_english(frenchText)
        self.assertEquals(transatedText, "Hello")

    def test_translateHello(self):
        frenchText = 'Hello'
        transatedText = translator.french_to_english(frenchText)
        self.assertEquals(transatedText, "Hello")