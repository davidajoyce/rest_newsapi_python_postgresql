import rest_newsapi as rnews


def main():
	
	url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=97c9e17e34af48ba9768758c481e45f3')

	rnews.create_url_info(url)




if __name__=='__main__':

	main()
