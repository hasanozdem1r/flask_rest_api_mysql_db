from app import app
# pip install Flask-MySQL==1.5.2
from flaskext.mysql import MySQL

mysql_object = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'ronwell_case_study'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql_object.init_app(app)
