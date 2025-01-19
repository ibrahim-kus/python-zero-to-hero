import sqlite3
import pandas as pd

#dataframe = pd.read_csv('datasets/sample.csv')
#dataframe = pd.read_json('datasets/sample.json', encoding="UTF-8")
#dataframe = pd.read_excel('datasets/sample.xlsx')

connection = sqlite3.connect("datasets/sample.db")
dataframe = pd.read_sql_query("Select * from students",connection)
print(dataframe)