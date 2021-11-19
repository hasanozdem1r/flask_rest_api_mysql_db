from app import app
import pymysql
from flaskext.mysql import MySQL # version Flask-MySQL==1.5.2

# create a MySQL class instance
mysql_object = MySQL()

# To configure access to your MySQL database server by using these settings
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Hsn58.34'
app.config['MYSQL_DATABASE_DB'] = 'ronwell_case_study'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# connect mysql_object with app
mysql_object.init_app(app)

def create_record(sql_query:str,data:tuple):
    connection = mysql_object.connect()
    db_cursor = connection.cursor()
    db_cursor.execute(sql_query, data)
    connection.commit()
    return db_cursor,connection

def connect_db():
    connection = mysql_object.connect()
    db_cursor = connection.cursor()
    return connection, db_cursor


# this section has been created testing connection independently
if __name__=='__main__':
    try:
        mysql_object.connect()
        print('Connection Successful')
        connection = mysql_object.connect()
    except Exception as error:
        print(f'Connection failed error message: {error}')