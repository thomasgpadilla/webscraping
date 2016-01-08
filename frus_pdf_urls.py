from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#point to FRUS volume page
html = urlopen("http://digicoll.library.wisc.edu/cgi-bin/FRUS/FRUS-idx?type=header&id=FRUS.FRUS1932v05")
soup = BeautifulSoup(html, 'html.parser')

with open("fdr_pdf_urls.txt", "w") as file:

#scrape FRUS volume section relative URLs 
	for links in soup.find_all("p", {"class":"cntsitem"}):

#prepend relative URLs with base URL
		for link in links.find_all('a'):
			itempageurl = 'http://digicoll.library.wisc.edu/' + link.get('href')

			pdfurls = requests.get (itempageurl)
			pdfsoup=BeautifulSoup(pdfurls.content, 'html.parser')
			
#visit each FRUS volume section page and scrape the PDF item URL and write to a TXT file
		for pdfurls in pdfsoup.find_all("div", {"class":"itemmd"}):
				for item in pdfurls.find_all('a'):
					print (item.get('href'))
					file.write(item.get('href')+"\n")

