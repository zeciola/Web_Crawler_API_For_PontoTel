from flask import Flask , request, jsonify
from web_crawler import wc
import json

app = Flask(__name__)

@app.route('/')
def HelloFask():
    #This method serves as the default API
   return jsonify({"send" : "hello flask"})


@app.route('/aw')
def aw():
    '''
    This method serves as the route for using the API
    '''
    word = request.args['word']
    url = request.args['url']
    num = 0
    num_url = 0
    urls = url.split(',')
    list_results = []

    if len(urls) >= 2:

        i = 0

        for i in range(0,len(urls)):

            num_url = wc.Amount_words(word,urls[i]).amount_words_result()

            num += wc.Amount_words(word,urls[i]).amount_words_result()

            dict_json = {'url': urls[i], 'result': num_url}

            list_results.append(dict_json)

        list_results.append({'total_result': num})

        return jsonify(list_results)
    else:
        num = wc.Amount_words(word,url).amount_words_result()
        return jsonify({"url":url,"result": num})

#http://127.0.0.1:5000/aw?word=Netflix&url=http://www.adorocinema.com/noticias/series/noticia-144072/

#http://127.0.0.1:5000/aw?word=Netflix&url=https://noticias.uol.com.br/cotidiano/ultimas-noticias/2018/10/17/mega-sena-pode-pagar-r-25-milhoes-nesta-quarta-feira.htm,http://agenciabrasil.ebc.com.br/geral/noticia/2018-10/conselho-do-tse-para-noticias-falsas-faz-reuniao-com-whatsapp,https://oglobo.globo.com/brasil/mpf-abre-investigacao-sobre-noticias-falsas-envolvendo-urnas-eletronicas-23159614

if __name__ == '__main__':
    app.run(debug=True)