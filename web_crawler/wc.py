from bs4 import BeautifulSoup as bs , UnicodeDammit
from requests import get
import unicodedata

class Amount_words():

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

        import ipdb ; ipdb.set_trace()

        page_text_S_len = len(page_text_S)

        cont = 0
        
        for i in range(page_text_S_len - 1):
            if page_text_S[i] == self.word:
                cont += 1
                
        return cont

