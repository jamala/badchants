import json
import pronouncing
import re
import random

CELEBS_PATH = 'input/celebrities.json'

def load_names():
	celebs = ""
	with open(CELEBS_PATH) as f:
		file_data = f.read()
		celebs = json.loads(file_data)
	return celebs['celebrities']


def matches_stress_pattern(string, pattern):
	stresses = pronouncing.stresses_for_word(string)
	regexp = re.compile(pattern)
	return any(map(regexp.search, stresses))

def all_match_cadence(strings, patterns):
	return len(strings) == len(patterns) and all(map(matches_stress_pattern, strings, patterns))

def has_wrestling_cadence(string):
	words = string.split()
	if len(words) == 2:
		return all_match_cadence(words, ['^[12]0$'] * 2)
	return False

def make_chant(string):
	clap = "\U0001F44F"
	half_chant = f"{string.upper()}! {clap} {clap} {clap}{clap}{clap}"
	return "\n".join([half_chant] * 2)


if __name__ == '__main__':
	names = load_names()
	filtered_names = list(filter(has_wrestling_cadence, names))
	print(make_chant(random.choice(filtered_names)))