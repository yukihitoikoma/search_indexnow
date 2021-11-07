import configparser, requests, json, argparse
from time import sleep

# load config settings
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

SEARCH_ENGINE_LIST = config_ini['DEFAULT']['SEARCH_ENGINE_LIST']
DOMAIN = [config_ini['WEBSITE1']['DOMAIN'], config_ini['WEBSITE2']['DOMAIN']]
API_KEY = [config_ini['WEBSITE1']['API_KEY'], config_ini['WEBSITE2']['API_KEY']]

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--urls', nargs='*')
args = parser.parse_args()

host = args.host
urls = args.urls
for engine in SEARCH_ENGINE_LIST:
    ENDPOINT = f"https://{engine}/indexnow"
    n = 0 if host == DOMAIN[0] else 1
    for url in urls:
        requests.post(
            ENDPOINT,data=json.dumps({
                "host" : host,
                "key" : API_KEY[n],
                "keyLocation" : f"https://{host}/{API_KEY[n]}.txt",
                "urlList" : [url] 
            })
        )
        sleep(5)