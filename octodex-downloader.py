from bs4 import BeautifulSoup
import urllib
import wget
import os

link = "https://octodex.github.com/"
page = urllib.urlopen(link)
soup = BeautifulSoup(page.read(), "html.parser")

octodex_list = "octodex_list.txt"

image_tags = soup.findAll('img', {"data-src": True})

try:
	os.remove(octodex_list)
except OSError:
	pass

with open("octodex_list.txt", "w") as avatar_list:
	# os.mkdir("avatars")
	os.chdir("avatars")
	for tag in image_tags:
		image_link = link[:-1] + str(tag['data-src'])
		wget.download(image_link)
		avatar_list.write(image_link)