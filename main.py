import sqlite3 as s3
import json
from datetime import datetime

timeframe = '2015-01'
sql_transaction = []

connection = s3.connect('{}.db'.format(timeframe))
cur = connection.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

if __name__ == "__main__":
    create_table()