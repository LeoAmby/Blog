import unittest 
from quote import Quote


class TestQuote(unittest.TestCase):
    def setUp(self):
    self.new_quote = Quote("38", "Alan Kay", "software today is very much like an Egyptian pyramid", "http://quotes.stormconsultancy.co.uk/quotes/38")
    
    
    def test_init(self):
    self.assertEqual(self.new_quote.id,"38")
    self.assertEqual(self.new_quote.author,"Alan Kay")
    self.assertEqual(self.new_quote.quote, "software today is very much like an Egyptian pyramid")
    self.assertEqual(self.new_quote.url, "http://quotes.stormconsultancy.co.uk/quotes/38")


if __name__ == '__main__':
    unittest.main()


