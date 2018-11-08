from sanic import Sanic, request
from sanic.response import json
from web_crawler import wc

app = Sanic()

@app.route("/")
async def AsyHelloSanic(request):
    return json({"hello": "sanic"})


@app.route("/aw")
async def Aw(request):
    '''
    This method serves as the route for using the API
    '''
    word = request.args['word']
    word = word[0]
    url = request.args['url']
    num = 0
    num_url = 0
    urls = url[0].split(',')    
    list_results = []

    if len(urls) >= 2:

        i = 0

        for i in range(0,len(urls)):

            num_url = wc.Amount_words(word,urls[i]).amount_words_result()

            num += wc.Amount_words(word,urls[i]).amount_words_result()

            dict_json = {'url': urls[i], 'result': num_url}

            list_results.append(dict_json)

        list_results.append({'total_result': num})

        return json(list_results)
    else:
        num = wc.Amount_words(word,url).amount_words_result()
        return json({"url":url,"result": num})

if __name__ == "__main__":
    app.run(debug=True ,host="127.0.0.2", port=8000)
