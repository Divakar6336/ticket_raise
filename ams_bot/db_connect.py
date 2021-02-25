import pymysql.cursors
import pymysql
from datetime import datetime


# Connect to the database

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='ticket',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor() 

def insert_ticket(type,description):
    # insert a single record
    sql = """INSERT INTO ticket (type,description,date) VALUES(%s, %s, %s)"""
    date=datetime.today().strftime('%Y-%m-%d')
    result=cursor.execute(sql,(type,description,date))
    # print(result)
    if result is not None:
        connection.commit()
        return 'Ticket Raised'
    else:
        return 'Request Not Accepted' 


        