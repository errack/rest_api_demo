import unittest
import sys
import os

sys.path.insert(0,'bin')

from url_parsing import URLParsing
from analyzer import Analyzer

class TestUrlAnalyzer(unittest.TestCase):

    def setUp(self):
        self.url_link = "https://www.paginasamarillas.com.pe/departamento-junin/servicios/repuestos-para-motocicleta"
    
    def test_request_parsing(self):
        keywords = URLParsing(self.url_link)
        print(keywords)
        self.assertEquals(type(keywords),URLParsing)

    def test_unique_keywords(self):
        keywords = URLParsing(self.url_link).unique_kw()
        print(keywords)
        self.assertEquals(len(keywords.get("keyword")),18)

    def test_kw_in_tittle(self):
        keywords = URLParsing(self.url_link).kw_in_tittle()
        print(keywords)
        self.assertEquals(len(keywords.get('keywords')),4)
  
    def test_frequency_kw(self):
        kw = URLParsing(self.url_link).frequency_kw()
        print(kw)


if __name__ == "__main__":
    main()
