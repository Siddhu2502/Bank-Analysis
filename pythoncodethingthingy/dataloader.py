import csv
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql://siddharth:Best#123@localhost/bankloandb')

df = pd.read_csv("Excel_file_name.csv",sep=',',quotechar='\'',encoding='utf8')
df.to_sql('bankloan', con=engine,index=False, if_exists='append') 