import psycopg2



def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE news (
            news_id SERIAL PRIMARY KEY,
            news_source VARCHAR(255) ,
	    news_title VARCHAR(255) ,
	    news_url VARCHAR(255) ,
	    news_description VARCHAR(255),
	    news_publishedAt VARCHAR(255) 		
        )
        """,
        
       )
    conn = None
    try:
        
        # connect to the PostgreSQL server   
	conn = psycopg2.connect(host="localhost",database="newsapi", user="postgres", password="postgres")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_news_list(news_list):
    """ insert multiple newsapi info from newsapi response  """
    sql = "INSERT INTO news(news_source, news_title, news_url, news_description, news_publishedAt) VALUES(%s,%s,%s,%s,%s)"
    conn = None
    try:
      
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="localhost",database="newsapi", user="postgres", password="postgres")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,news_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
if __name__ == '__main__':
    	
	create_tables()

	




