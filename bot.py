from badchants import has_wrestling_cadence, make_chant
from mastodon import Mastodon
import json
import sys
import random

CELEBS_PATH = 'input/celebrities.json'

def load_names():
	celebs = ""
	with open(CELEBS_PATH) as f:
		file_data = f.read()
		celebs = json.loads(file_data)
	return celebs['celebrities']

def main():
	access_token = sys.argv[1]
	api = Mastodon(access_token = access_token, api_base_url = 'https://botsin.space')
	wrestling_names = list(filter(has_wrestling_cadence, load_names()))
	status_text = make_chant(random.choice(wrestling_names))
	print(status_text)
	status = api.status_post(status_text)
	print(f"status posted at {status['url']}")

if __name__ == '__main__':
	main()

