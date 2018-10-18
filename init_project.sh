#!/bin/zsh

mkvirtualenv -p python3 Web_Crawler_PontoTel

work_on Web_Crawler_PontoTel

pip install -r dev_requirements

python app.py

pytest test/test_*.py

