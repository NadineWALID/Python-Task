import mysql.connector
 

dataBase = mysql.connector.connect(
                     host = "localhost",               
                     user = "root",                   #enter user
                     passwd = "",                     #enter password
                     database = "geeks4geeks" )      #enter database created for table
 

cursorObject = dataBase.cursor()

createTable = """CREATE TABLE Inventory (
                   Id  INT NOT NULL AUTO_INCREMENT ,
                   Name VARCHAR(50) NOT NULL,
                   Description VARCHAR(255),
                   Quantity INT,
                   Price FLOAT,
                   PRIMARY KEY (Id)
                   )"""
cursorObject.execute(createTable)
 

insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #1', 'This is Item #1', '1', '199.99')"""
cursorObject.execute(insertDB)
insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #2', 'This is Item #2', '10', '50')"""
cursorObject.execute(insertDB)
insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #3', 'This is Item #3', '2', '100')"""
cursorObject.execute(insertDB)
insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #4', 'This is Item #4', '5', '60.99')"""
cursorObject.execute(insertDB)
insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #5', 'This is Item #5', '6', '70.50')"""
cursorObject.execute(insertDB)
insertDB = """INSERT INTO `inventory` (`Id`, `Name`, `Description`, `Quantity`, `Price`) 
VALUES (NULL, 'Item #6', 'This is Item #6', '12', '20')"""
cursorObject.execute(insertDB)

dataBase.commit()
dataBase.close()