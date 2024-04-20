import unittest
from bs4 import BeautifulSoup

def obtener_texto_h1(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')
    return h1.get_text() if h1 else None

class TestIndexHTML(unittest.TestCase):
    def test_texto_h1(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            html = file.read()
        texto_h1 = obtener_texto_h1(html)
        self.assertEqual(texto_h1, 'Práctica Final de DevOps')

if __name__ == '__main__':
    unittest.main()