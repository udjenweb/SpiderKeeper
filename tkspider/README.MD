https://github.com/DormyMo/SpiderKeeper#usage


запускаем SpiderKeeper
создаем новый проект tkspider
http://0.0.0.0:5000/project/1/spider/deploy



создаем egg для подключения к  SpiderKeeper
Use scrapyd-client to generate egg file
    https://github.com/scrapy/scrapyd-client
    (создаст 2а файла: setup.py, tkspider.egg)
    scrapyd-deploy --build-egg tkspider.egg
*!* редактируем  setup.py, - ставим версию 'v1.0'

запускаем демон для скрапи парсеров
https://scrapyd.readthedocs.io/en/stable/
https://scrapyd.readthedocs.io/en/stable/overview.html#starting-scrapyd
    pip install scrapyd
    scrapyd
http://localhost:6800/


добовляем tkspider
https://scrapyd.readthedocs.io/en/stable/deploy.html
http://scrapyd.readthedocs.io/en/stable/api.html?highlight=addversion.json%20-F%20project#addversion-json
curl http://localhost:6800/addversion.json -F project=tkspider -F version='v1.0' -F egg=@tkspider.egg


добовляем полученный файл
http://0.0.0.0:5000/project/1/spider/deploy