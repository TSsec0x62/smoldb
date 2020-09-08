import requests
import sys
if len(sys.argv) != 3:
	print("Usage: python3 <url> <path/to/wordlist.txt>\nNote: Include the trailing / in the URL")
	exit()
with open(sys.argv[2]) as open_file:
	word_list = open_file.readlines()
cleaned_word_list = [item.rstrip('\n') for item in word_list]
responses = [requests.get(sys.argv[1] + item)  for item in cleaned_word_list]
[print(str(item.status_code) + ": " + str(item.url)) for item in responses if item.status_code == 200]