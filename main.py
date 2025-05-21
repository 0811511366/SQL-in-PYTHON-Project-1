import sqlite3

basketball='basketball.sqlite'

conn = sqlite3.connect(basketball)
print("opened data successfully!!")

import pandas as pd
cursor=conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(tables)