from unittest import TestCase
from requests import get

import app

url = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm'

word = 'isso'

urls = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm,https://noticias.r7.com/economia/novo-saque-do-pispasep-e-liberado-nesta-quinta-feira-18102018,https://noticias.r7.com/economia/pagamento-do-13-salario-injeta-r-2112-bilhoes-na-economia-18102018'


test_url = 'http://127.0.0.1:5000/'

test_url_aw = 'http://127.0.0.1:5000/aw?word=Netflix&url=http://www.adorocinema.com/noticias/series/noticia-144072/'

test_url_json = {'send': 'hello flask'}

test_url_json_aw = {'result': 11}

class Test_AW(TestCase):

    def test_api_conection(self):
        self.assertEqual(get(test_url).status_code, 200, msg='/ is ok')

    def test_api_conection_aw(self):
        self.assertEqual(get(test_url_aw).status_code, 200, msg='/aw?word=any&url=any_url is ok')

    def test_api_json(self):
        self.assertDictEqual(get(test_url).json(), test_url_json, msg=f'/ json is ok return {test_url_json}')

    def test_api_json_aw(self):
        self.assertDictEqual(get(test_url_aw).json(), test_url_json_aw, msg=f'/aw?word=any&url=any json is ok return {test_url_json_aw}')



