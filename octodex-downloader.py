from bs4 import BeautifulSoup
from urllib.request import urlopen
import wget
import os
import csv

link = "https://octodex.github.com/"

with urlopen(link) as url:
	soup = BeautifulSoup(url.read(), "html.parser")

octocat_list = "octodex_list.txt"

image_tags = soup.findAll('img', {"data-src": True})
print("Found", len(image_tags), "octocats.\n")

try:
	os.remove(octocat_list)
except OSError:
	pass

with open("octodex_list.txt", "w") as octocat_list:
	if not os.path.exists("octocats"):
		os.mkdir("octocats")
	os.chdir("octocats")

	csvWriter = csv.writer(octocat_list)
	csvWriter.writerow(['name', 'url'])

	for tag in image_tags:
		octocat_image_link = link[:-1] + str(tag['data-src'])
		octocat_name = str(tag['alt'])
		wget.download(octocat_image_link, out = octocat_name + str(tag['data-src'])[-4:], bar = None)
		print("Downloaded", octocat_name)
		csvWriter.writerow([octocat_name, octocat_image_link])

print("\nDownloaded all", len(image_tags), "octocats.")