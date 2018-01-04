#!/usr/bin/env python3

import psycopg2

# QUERIES
# What are the most popular articles of all time?
query_articles = """SELECT articles.title, count(*) AS views
           FROM articles JOIN log
           ON log.path
           LIKE concat('%', articles.slug, '%')
           WHERE log.status LIKE '200 OK'
           GROUP BY articles.title
           ORDER BY views DESC
           LIMIT 3;"""


# Who are the most popular authors of all time?
query_authors = """SELECT authors.name, count(*) AS views
           FROM authors JOIN articles
           ON authors.id = articles.author
           INNER JOIN log
           ON log.path LIKE concat('/article/%', articles.slug)
           GROUP BY authors.name
           ORDER BY views DESC LIMIT 3;"""

# On which days did more than 1 percent of requests lead to errors?
query_errors = """SELECT requests.date,
           round((err_requests.total*1.0) / (requests.total)*100, 2)
           AS percent
           FROM requests, err_requests
           WHERE err_requests.date = requests.date
           AND (round((err_requests.total*1.0) / (requests.total)*100, 2)) > 1
           ORDER BY percent
           LIMIT 3;"""

DBNAME = "news"

# Connect to the database,run query and return results.


def db_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Get the most popular views.
def get_popular_articles():
    popular_articles = db_query(query_articles)
    print('\n \n ----MOST POPULAR ARTICLES ---- \n')

    for article in popular_articles:
        print("%s ---- %s views" % (article[0], article[1]))


# Get the most popular views.
def get_popular_authors():
    popular_authors = db_query(query_authors)
    print('\n \n ----MOST POPULAR AUTHORS----- \n')

    for author in popular_authors:
        print("%s ----- %s views" % (author[0], author[1]))


# Get the days with most 404 errors.
def get_day_errors():
    day_errors = db_query(query_errors)
    print('\n \n ----DAY WITH MOST ERRORS---- \n')

    for error in day_errors:
        print("%s ---- %s percent" % (error[0], error[1]))


# Print out the results
get_popular_articles()
get_popular_authors()
get_day_errors()