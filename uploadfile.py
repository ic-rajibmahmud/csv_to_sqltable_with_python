import csv
import pyodbc
import os
from glob import glob
from time import time

t1 = time()
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=Server address;'
                      'DATABASE=DBname;'
                      'UID=SA;'
                      'PWD=******')


cursor = conn.cursor()
customer_data = csv.reader('cleanNVG.csv') #25 columns with same header as SQL
PATH = "location"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]


for file_to_import in all_csv_files:
    with open(file_to_import) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            print(row)
            cursor.execute("INSERT INTO dbo.secondarysalesdata(Sales_Year,Sales_Month,RegionCode,Town,PH10Code,ChannelCode,OutletCode,TradeSalesValue,SalesQty) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",row)
            conn.commit()

 


conn.close()


conn.commit()
cursor.close()
print("alldone")
t2 = time()

print(f'Took {t2-t1} ms')
