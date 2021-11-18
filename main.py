import pymysql
from database_config import mysql_object
from app import app
from flask import Flask, jsonify, request,abort




# GET all categories
@app.route('/api/v1/categories')
def show_all_categories():
    try:
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM category_table")
        authors=db_cursor.fetchall()
        response = jsonify(authors)
        response.status_code = 200
        return response
    except Exception as error:
        print(error)
    finally:
        db_cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run()