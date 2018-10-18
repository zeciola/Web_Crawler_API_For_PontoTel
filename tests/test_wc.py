from unittest import TestCase

from web_crawler import wc

url = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm'

word = 'isso'


class Test_WC(TestCase):

    def test_one_url(self):
        self.assertEqual(wc.Amount_words(word,url).amount_words_result(), 1)
        