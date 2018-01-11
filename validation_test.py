import rest_newsapi as rnews
import unittest

class test_url_validation(unittest.TestCase):
	
	def test_check_valid_http(self):
		self.assertTrue(rnews.is_URL_valid('https://google.com'))

	def test_check_invalid_http(self):
		self.assertFalse(rnews.is_URL_valid('http://invalidURL'))

if __name__ == '__main__':
	unittest.main()
