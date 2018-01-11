import urllib2
import sys
import requests

def is_URL_valid(URL):

	try:
		urllib2.urlopen(URL)		
		return True
	except ValueError, ex:
		sys.stderr.write("This URL is not valid")	
		return False
	except urllib2.URLError, ex:
		sys.stderr.write("This URL is not valid")
		return False


def create_tuple(article):
	tup = (article['source']['id'],article['title'],article['url'],article['description'],article['publishedAt'])

	return tup

def create_url_info(url):
	
	response = requests.get(url)
	json_dict = response.json()
	list_art = []

	for i in range(len(json_dict['articles'])):
		
		info_tuple = create_tuple(json_dict['articles'][i])
		list_art.append(info_tuple)

	

		









	



	
