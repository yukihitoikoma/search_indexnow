import configparser, requests, json, argparse

# load config settings
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

ENDPOINT = "https://api.indexnow.org/indexnow"
DOMAIN = [config_ini['WEBSITE1']['DOMAIN'], config_ini['WEBSITE2']['DOMAIN']]
API_KEY = [config_ini['WEBSITE1']['API_KEY'], config_ini['WEBSITE2']['API_KEY']]

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--urls', nargs='*')
args = parser.parse_args()

host = args.host
urls = args.urls

n = 0 if host == DOMAIN[0] else 1
api = API_KEY[n]
requests.post(
    ENDPOINT, data=json.dumps({
        "host" : host,
        "key" : api,
        "keyLocation" : f"https://{host}/{api}.txt",
        "urlList" : urls
    })
)
