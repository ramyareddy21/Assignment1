import sqlite3
import pandas as pd

conn = sqlite3.connect('XYZ_Sales.db')

Query = """SELECT C.Customer_ID, C.Age, I.Item_Name, SUM(O.Quantity) AS TotalQuantity
           FROM Customer C
           JOIN Sales S
           ON C.Customer_ID = S.Customer_ID
           CROSS JOIN Items I
           LEFT JOIN Orders O ON S.Sales_ID = O.Sales_ID AND I.Item_ID = O.Item_ID
           WHERE C.Age BETWEEN 18 AND 35
           GROUP BY C.Customer_ID, C.Age, I.Item_Name
           HAVING TotalQuantity > 0"""

df = pd.read_sql_query(Query, conn)

conn.close()

df.to_csv('C:/Users/ramya/OneDrive/Desktop/Eastvantage_Assignment/PandasOutput.csv', sep=';', index=False)