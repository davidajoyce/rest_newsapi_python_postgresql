import rest_newsapi as rnews
import sys


def main():

	input_file = sys.stdin.readlines()
	
	for line in input_file:
		url = line.strip()
		
		if rnews.is_URL_valid(url):
			rnews.create_url_info(url)

			



if __name__=='__main__':

	main()
