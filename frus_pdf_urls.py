from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen("http://digicoll.library.wisc.edu/cgi-bin/FRUS/FRUS-idx?type=header&id=FRUS.FRUS1932v05")
soup = BeautifulSoup(html, 'html.parser')

with open("fdr_pdf_urls.txt", "w") as file:

	for itemlinks in soup.find_all("p", {"class":"cntsitem"}):

		for link in itemlinks.find_all('a'):
			itemurl = 'http://digicoll.library.wisc.edu/' + link.get('href')

			pdfurl = requests.get (itemurl)
			pdfsoup=BeautifulSoup(pdfurl.content, 'html.parser')

		for pdflink in pdfsoup.find_all("div", {"class":"itemmd"}):
				for plink in pdflink.find_all('a'):
					print (plink.get('href'))
					file.write(plink.get('href')+"\n")

