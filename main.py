import pymysql
from database_config import mysql_object
from app import app
from flask import Flask, jsonify, request,abort


# GET all categories
# Example call format : curl http://127.0.0.1:5000/api/v1/categories
@app.route('/api/v1/categories')
def show_all_categories():
    try:
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM category_table")
        categories=db_cursor.fetchall()
        response = jsonify(categories)
        response.status_code = 200
        return response
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
        db_cursor.close()
        connection.close()

# GET category by name of category
# Example call format : curl http://127.0.0.1:5000/api/v1/categories?category_name
@app.route('/api/v1/categories')
def get_by_category_name():
    try:
        category_name:str=str(request.args.get('category_name'))
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM category_table")
        #db_cursor.execute("SELECT * FROM category_table WHERE category_name=%s",category_name)
        categories=db_cursor.fetchall()
        print(len(categories))
        response = jsonify(categories)
        response.status_code = 200
        return response
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
        db_cursor.close()
        connection.close()


# GET all authors
# Example call format : curl http://127.0.0.1:5000/api/v1/authors
@app.route('/api/v1/authors')
def show_all_authors():
    try:
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM author_table")
        authors=db_cursor.fetchall()
        response = jsonify(authors)
        response.status_code = 200
        return response
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
        db_cursor.close()
        connection.close()

# GET all blogs
# Example call format : curl http://127.0.0.1:5000/api/v1/blogs
@app.route('/api/v1/blogs')
def show_all_blogs():
    try:
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM blog_table")
        blogs=db_cursor.fetchall()
        response = jsonify(blogs)
        response.status_code = 200
        return response
    except Exception as error:
        error_dict = {'Error': str(error)}
        return jsonify(error_dict)
    finally:
        db_cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run()