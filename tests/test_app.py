from unittest import TestCase
from requests import get

import app

url = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm'

word = 'isso'

urls = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm,https://noticias.r7.com/economia/novo-saque-do-pispasep-e-liberado-nesta-quinta-feira-18102018,https://noticias.r7.com/economia/pagamento-do-13-salario-injeta-r-2112-bilhoes-na-economia-18102018'

test_url = 'http://127.0.0.1:5000/'

test_url_aw = 'http://127.0.0.1:5000/aw?word=Netflix&url=http://www.adorocinema.com/noticias/series/noticia-144072/'

test_mult_url_aw = 'http://127.0.0.1:5000/aw?word=Netflix&url=http://www.adorocinema.com/noticias/series/noticia-144072/,https://mundoconectado.com.br/noticias/v/7202/netflix-considera-baixar-preco-da-mensalidade-para-conseguir-mais-assinantes,https://cinepop.com.br/the-princess-switch-vanessa-hudgens-e-uma-princesa-em-novo-filme-da-netflix-confira-a-imagem-191529'

test_url_json = {'send': 'hello flask'}

test_url_json_aw = {'result': 11, 'url': 'http://www.adorocinema.com/noticias/series/noticia-144072/'}

test_mult_url_json_aw = [{'result': 11, 'url': 'http://www.adorocinema.com/noticias/series/noticia-144072/'}, {'result': 1, 'url': 'https://mundoconectado.com.br/noticias/v/7202/netflix-considera-baixar-preco-da-mensalidade-para-conseguir-mais-assinantes'}, {'result': 2, 'url': 'https://cinepop.com.br/the-princess-switch-vanessa-hudgens-e-uma-princesa-em-novo-filme-da-netflix-confira-a-imagem-191529'}, {'total_result': 14}]

class Test_AW(TestCase):
    '''
    This class is for testing the API
    '''

    def test_api_conection(self):
        '''
        This method is to verify that the connection to / is working code 200
        '''
        self.assertEqual(get(test_url).status_code, 200, msg='/ is not ok')

    def test_api_conection_aw(self):
        '''
        This method is to verify that the connection to /aw is working code 200
        '''
        self.assertEqual(get(test_url_aw).status_code, 200, msg='/aw?word=any&url=any_url is not ok')

    def test_api_json(self):
        '''
        This method is to check if the json of / is correstodent
        '''
        self.assertDictEqual(get(test_url).json(), test_url_json, msg=f'/ json is not ok, return {test_url_json}')

    def test_api_json_aw(self):
        '''
        This method is to check if the json of /aw is correstodent
        '''
        self.assertDictEqual(get(test_url_aw).json(), test_url_json_aw, msg=f'/aw?word=any&url=any json is not ok, return {test_url_json_aw}')

    def test_api_mult_json_aw(self):
        '''
        This method is used to verify that the json of / is corresponding to the multiple urls
        '''
        self.assertEqual(get(test_mult_url_aw).json(), test_mult_url_json_aw)
        
