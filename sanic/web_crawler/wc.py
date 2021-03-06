from bs4 import BeautifulSoup as bs
from requests import get
import unicodedata

class Amount_words():
    '''
    This is the class that works as web crawler
    '''

    def __init__(self, word, url):
         self.word = word
         self.url = url

    def get_page_text(self):

        page_source = get(self.url).text

        bs_obj = bs(page_source, "html.parser")

        box = bs_obj.find("html")

        page_text = box.text

        page_text = unicodedata.normalize("NFKD", page_text)

        return page_text

    def amount_words_result(self):

        page_text_S = str(self.get_page_text()).strip('/n').strip('/t').replace(',', ' ').replace('.', ' ').split()

        page_text_S_len = len(page_text_S)

        cont = 0

        i = 0

        for i in range(0,page_text_S_len):
            if page_text_S[i] == self.word:
                cont += 1
                
        return cont

