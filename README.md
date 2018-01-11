# rest_newsapi_python_postgresql
This is a python script to request the top news stories from various new sites and store them in a postgresql table.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installing

This python script was developed using python 2.7.12, make sure the correct version is installed

Make sure the following python modules are installed. Install the following python module using the following command lines:

```
pip install unittest
pip install psycopg2
pip install urllib2
pip install sys
pip install requests

```

## Running the tests

To run the unit tests:

```
python validation_test.py
```

## Running the program:

To run the program:

Use the following command line:
```
cat input.txt | python main.py
```

To edit the news sources in the urls for top stories please edit the source below (e.g this case it is **techcrunch**) in the url to the available news sources in the link [newsapi](https://newsapi.org/sources):

https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=97c9e17e34af48ba9768758c481e45f3


## Storing the info in a Postgresql database

install pgadmin III for a graphical interface to create the database

## Create the newsapi table in Postgresql

Use the following command line:
```
python python_postgresql.py
```




