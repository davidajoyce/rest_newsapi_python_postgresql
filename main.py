import rest_newsapi as rnews
import sys


def main():
	'''
	url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=97c9e17e34af48ba9768758c481e45f3')
'''

	input_file = sys.stdin.readlines()
	
	for line in input_file:
		url = line.strip()

		rnews.create_url_info(url)
	

	#rnews.create_url_info(url)




if __name__=='__main__':

	main()
