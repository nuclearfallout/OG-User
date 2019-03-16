# Basic OG User tool
# Generates random string of chars/numbers
# Forwords to selected platform URL
# returns if taken/available

# Make for linux enviornment haven't tested on windows

# Known issues: Returns banned accounts as available


import requests, sys, string, time, os

from random import *

import random

from random import choice



print("- Which platform? - ")

print("1. Instagram")

print("2. Twitter")
print("3. Twitch")


platformSelect = raw_input("->  ")


def main(name):

	if platformSelect == "1":

		url = "https://www.instagram.com/%s" % (name)

		output = "availableIG.txt"

	if platformSelect == "2":

		url = "http://twitter.com/%s" % (name)

		output = "availableTwitter.txt"

	if platformSelect == "3":
		url = "http://www.twitch.tv/%s" % (name)
		output = "availableTwitch.txt"
	r = requests.get(url)

	data = r.text



	if "Sorry" in data:

		print "\033[1;31m[\033[1;37m%s\033[1;31m] -> [\033[1;32mAvalible\033[1;31m]" % (url)

		os.system("echo '%s' >> %s" % (name, output))

	else:

		print("\033[1;31m[\033[1;37m%s\033[1;31m] -> [\033[1;30mTaken\033[1;31m]" % (url))	


while True:

	chars = "abcdefghijklmnopqrstuvwxyz1234567890"

	usr = "".join(random.choice(chars) for x in range(randint(3, 5)))

	main(usr)


