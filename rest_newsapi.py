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





	



	
