import sqlite3
import csv

con_Obj = sqlite3.connect('XYZ_Sales.db')
cur_Obj = con_Obj.cursor()

cur_Obj.execute("""SELECT C.Customer_ID, C.Age, I.Item_Name, SUM(O.Quantity) AS TotalQuantity
           FROM Customer C
           JOIN Sales S
           ON C.Customer_ID = S.Customer_ID
           CROSS JOIN Items I
           LEFT JOIN Orders O ON S.Sales_ID = O.Sales_ID AND I.Item_ID = O.Item_ID
           WHERE C.Age BETWEEN 18 AND 35
           GROUP BY C.Customer_ID, C.Age, I.Item_Name
           HAVING TotalQuantity > 0""")


results = cur_Obj.fetchall()
print(results)

con_Obj.close()

with open('C:/Users/ramya/OneDrive/Desktop/Eastvantage_Assignment/SQLOutput.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])
    csv_writer.writerows(results)

print(f'Data has been written to the file!')
