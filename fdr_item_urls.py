#purpose: 1. grab item specific URLs links to feed to WGET 2. save results to txt OR csv 
#usecase: Franklin D. Roosevelt, Master Speech File, 1898-1945 | Franklin D. Roosevelt Presidential Library & Museum

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen("http://www.fdrlibrary.marist.edu/archives/collections/franklin/index.php?p=collections/findingaid&id=582")
soup = BeautifulSoup(html, 'html.parser')


#save to TXT

with open("fdr_item_urls.txt", "w") as file:
	for itemlinks in soup.find_all("dd", {"class":"faitemcontent"}):
		for link in itemlinks.find_all('a'):
			print (link.get('href'))
			file.write(link.get('href')+"\n")


#save to CSV

#csvFile=open("fdr_item_urls.csv", 'wt')
#writer=csv.writer(csvFile)

#with open("fdr_item_urls.csv", "wt") as csvFile:
#	writer=csv.writer(csvFile)
#	for itemlinks in soup.find_all("dd", {"class":"faitemcontent"}):
#		for link in itemlinks.find_all('a'):
#			print (link.get('href'))
#			writer.writerow([link['href']])




