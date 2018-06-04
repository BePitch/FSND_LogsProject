#!/usr/bin/env python3
# Database code for the News DataBase .
import psycopg2
from datetime import datetime
# Databse global variable
DBNAME = "news"


# Build out the use for returning the articles report
def report_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(open("topViewArticles.sql", "r").read())
    reportArticles = c.fetchall()
    # build output format
    print("Top 3 articles viewed all time")
    print("\n")
    print("Article Name      |     Views    ")
    for i in reportArticles:
        print(str(i[0]) + ' -- ' + str(i[1]))
    print("\n")
    db.close()
    return reportArticles


# Build out the use for returning the author report
def report_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(open("topAuthors.sql", "r").read())
    reportAuthors = c.fetchall()
    # build output format
    print("Top authors viewed all time")
    print("\n")
    print("Author Name    |   Views  ")
    for i in reportAuthors:
        print(str(i[0]) + ' -- ' + str(i[1]))
    print("\n")
    db.close()
    return reportAuthors


# Build out the use for returning the error report
def report_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(open("errorsDaily.sql", "r").read())
    reportErrors = c.fetchall()
    # build output format
    print("Days with an error rate >= 1%")
    print("\n")
    print("Error Date    | Rate of error  ")
    for i in reportErrors:
        print((i[0]).strftime('%B %d, %Y') + ' | ' + str(i[4]) + '%')
    print("\n")
    db.close()
    return reportErrors

if __name__ == "__main__":
    report_articles()
    report_authors()
    report_errors()
