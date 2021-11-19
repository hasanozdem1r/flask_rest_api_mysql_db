from app import app
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

# this section has been created testing connection independently
if __name__=='__main__':
    try:
        mysql_object.connect()
        print('Connection Successful')
    except Exception as error:
        print(f'Connection failed error message: {error}')