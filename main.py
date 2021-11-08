import configparser, requests, json, argparse
from time import sleep

# load config settings
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

SEARCH_ENGINE_LIST = json.loads(config_ini.get('DEFAULT', 'SEARCH_ENGINE_LIST'))
DOMAIN = [config_ini['WEBSITE1']['DOMAIN'], config_ini['WEBSITE2']['DOMAIN']]
API_KEY = [config_ini['WEBSITE1']['API_KEY'], config_ini['WEBSITE2']['API_KEY']]

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--urls', nargs='*')
args = parser.parse_args()

host = args.host
urls = args.urls
for url in urls:    
    n = 0 if host == DOMAIN[0] else 1
    api = API_KEY[n]
    for engine in SEARCH_ENGINE_LIST:
        ENDPOINT = f"https://{engine}/indexnow"
        requests.post(
            ENDPOINT, data=json.dumps({
                "host" : host,
                "key" : api,
                "keyLocation" : f"https://{host}/{api}.txt",
                "urlList" : [url] 
            })
        )
    sleep(5)