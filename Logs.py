#!/usr/bin/env python3

import psycopg2


DBNAME = "news"

def getData(query):
    """ fetches data from database """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def listPopularArticles():
    """ display the 3 most popular articles  """
   
    query = """
    select title, count(*) as num
    from articles, log
    where log.path like '%' || articles.slug
    group by title
    order by num desc
    """
    result = getData(query)[:3]
    print('⋅The most popular three articles of all time:')
    for record in result:
        print('"{}" - {} views'.format(record[0], record[1]))


def listPopularAuthors():
    """ display the popular authors """
    query = """
    select name, count(*) as num
    from authors, articles, log
    where authors.id = articles.author and log.path like '%' || articles.slug
    group by name
    order by num desc
    """
    result = getData(query)
    print('⋅The most popular article authors of all time:')
    for record in result:
        print('{} - {} views'.format(record[0], record[1]))


def listDaysWithError(per):
    """ display the days with error more than per% """
    
    query = 'select * from rate_of_error where rate >' + str(per)

    result = getData(query)
    print('⋅Days with error rate above ' + str(per) + '%:')
    for record in result:
        print('{} - {}% errors'.format(record[0], record[1]))


if __name__ == '__main__':
    print('[Analysis Report]')
    print('')
    listPopularArticles()
    print('')
    listPopularAuthors()
    print('')
    listDaysWithError(per=1)
    print('')