#!/usr/bin/env python2.7
from collections import defaultdict
from pwgen import pwgen
import sys


# Returns a dict with 3gram -> count
def get_3grams(lines):
	count_3gram = defaultdict(int)
	for word,count,typ in lines:
		if len(word) < 3:
			continue

		w = "^"+word+"$"
		for i in range(len(w)-2):
			count_3gram[w[i:i+3]] += count

	return count_3gram

# Replaces numbers with letters and adds first/last character.
def normalize_word(word):
	word = word.replace("1", "i")
	word = word.replace("2", "z")
	word = word.replace("3", "e")
	word = word.replace("4", "a")
	word = word.replace("5", "s")
	word = word.replace("8", "b")
	word = word.replace("0", "o")
	return "^"+word.lower()+"$"

# If a 3gram from given word is not in count_3gram, this function will
# return 0.
def rate_word(word):
	# there are no leet conversion of this numbers, so rate them as 0
	for b in "679":
		if b in word:
			return 0

	w = normalize_word(word)
	c = 1
	for i in range(len(w)-2):
		c *= count_3gram[w[i:i+3]]

	return c


if __name__ == '__main__':
	d = open("top1500_nouns.txt", "rb").read()
	lines = d.strip().split("\n")
	lines = map(lambda x:x.split(";"), lines)
	lines = map(lambda (w,c,t):(w,int(c),t.split(",")), lines)

	count_3gram = get_3grams(lines)

	max_word = ""
	max_c = 0

	length = 6
	print sys.argv
	if len(sys.argv) == 2:
		length = int(sys.argv[1])

	try:
		while True:
			word = pwgen(length).lower()
			# no starting number
			if word[0] in "0123456789":
				continue

			c = rate_word(word)
			if c > max_c:
				# print word with rating, if it's current maximum
				print word,c
				max_c = c
				max_word = word
			elif c > max_c/2**(len(word)-2):
				# print word with rating, if it's near current maximum
				print word,c
	except KeyboardInterrupt:
		pass

