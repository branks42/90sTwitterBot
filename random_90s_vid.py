import urllib.request
import urllib.parse
import re
import tweepy, time
import random
import webbrowser

while True:
	# Get songs from text file, put into a list and shuffle them
	list = []
	with open('90s_playlist.txt') as f:
		list = [x.strip('\n') for x in f.readlines()]
	random.shuffle(list)

	# Loop over playlist
	for song in list:
		# Get YouTube video id of the first search result
		query_string = urllib.parse.urlencode({"search_query" : song})
		html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

		# Print to console
		print("[" + time.ctime() + "] Song randomly chosen: " + song + "\nhttp://www.youtube.com/watch?v=" + search_results[0])

		# Open music video in chrome
		webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

		time.sleep(86400)