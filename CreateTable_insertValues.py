import sqlite3

con_Obj = sqlite3.connect('XYZ_Sales.db') # Connects to the SQLite database
cur_Obj = con_Obj.cursor() # To Interact with db

cur_Obj.execute("""CREATE TABLE Customer (Customer_ID INTEGER PRIMARY KEY,
                                          Age INTEGER)""") # Customer table

cur_Obj.execute("""CREATE TABLE Sales (Sales_ID INTEGER PRIMARY KEY,
                        Customer_ID INTEGER,
                        FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID))""") # Sales

cur_Obj.execute("""CREATE TABLE Items (Item_ID INTEGER PRIMARY KEY,
                          Item_Name TEXT)""") # Items

cur_Obj.execute("""CREATE TABLE Orders (Order_ID INTEGER PRIMARY KEY,
                                        Sales_ID INTEGER,
                                        Item_ID INTEGER,
                                        Quantity INTEGER NULL,
                                        FOREIGN KEY (Sales_ID) REFERENCES Sales(Sales_ID),
                                        FOREIGN KEY (Item_ID) REFERENCES Items(Item_ID))""") # Orders table

# Insert values
cur_Obj.execute('INSERT INTO Customer (Age) VALUES (21), (23), (35), (16), (42)')

cur_Obj.execute('''INSERT INTO Sales (Sales_ID, Customer_ID) VALUES (1, 1),
                                                                    (2, 2),
                                                                    (3, 1),
                                                                    (4, 3),
                                                                    (5, 1),
                                                                    (6, 3)''')

cur_Obj.execute("INSERT INTO Items (Item_Name) VALUES ('x'), ('y'), ('z')")

cur_Obj.execute("""INSERT INTO Orders (Sales_ID, Item_ID, Quantity) VALUES (1, 1, 2),   
                                                                           (1, 2, Null),
                                                                           (1, 3, Null),
                                                                           (2, 1, 1),
                                                                           (2, 2, 1),
                                                                           (2, 3, 1),
                                                                           (3, 1, 5),   
                                                                           (3, 2, Null),
                                                                           (3, 3, Null),
                                                                           (4, 1, Null),
                                                                           (4, 2, Null),
                                                                           (4, 3, 1),
                                                                           (5, 1, 3),
                                                                           (5, 2, Null),
                                                                           (5, 3, Null),
                                                                           (6, 1, Null),
                                                                           (6, 2, Null),
                                                                           (6, 3, 1)""")


con_Obj.commit()
con_Obj.close()

