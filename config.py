import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN=os.getenv('TOKEN')
AVAILABLE_UNITS = {'доллар': 'USD',  # словарь доступных валют
                       'рубль': 'RUB',
                       'йена': 'JPY',
                       'биткоин': 'BTC',
                        'евро':'EUR',
                   'юань':'CNY'}