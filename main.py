import configparser, requests, json, argparse

# load config settings
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

ENDPOINT = "https://api.indexnow.org/indexnow"
SETTINGS = {config_ini['WEBSITE1']['DOMAIN']: config_ini['WEBSITE1']['API_KEY'], config_ini['WEBSITE2']['DOMAIN']: config_ini['WEBSITE2']['API_KEY']}

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--urls', nargs='*')
args = parser.parse_args()

host = args.host
urls = args.urls

api = SETTINGS[host]
requests.post(
    ENDPOINT, data=json.dumps({
        "host" : host,
        "key" : api,
        "keyLocation" : "https://{0}/{1}.txt".format(host, api),
        "urlList" : urls
    })
)
