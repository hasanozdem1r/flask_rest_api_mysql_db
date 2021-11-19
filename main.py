import pymysql
from database_config import mysql_object
from app import app
from flask import Flask, jsonify, request,abort


# GET all categories
# Example call format : curl http://127.0.0.1:5000/api/v1/categories/all
@app.route('/api/v1/categories/all')
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
# Example call format : curl http://127.0.0.1:5000/api/v1/categories?category-name=Horrors
@app.route('/api/v1/categories')
def show_category():
    try:
        if 'category-name' in request.args:
            category_name:str=str(request.args.get('category-name'))
            connection = mysql_object.connect()
            db_cursor = connection.cursor(pymysql.cursors.DictCursor)
            db_cursor.execute("SELECT * FROM ronwell_case_study.category_table WHERE category_name=%s",category_name)
            categories=db_cursor.fetchone()
            response = jsonify(categories)
            response.status_code = 200
            return response
        else:
            info_msg = {'Information': str('Request format is not valid')}
            return jsonify(info_msg)
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
        db_cursor.close()
        connection.close()

# POST category
#In postman select post method -> http://127.0.0.1:5000/api/v1/category/put?category-name=FR&category-description=FR
@app.route('/api/v1/category/put',methods=['POST','GET'])
def add_category():
    try:
        if not 'category-name' in request.args or not 'category-description' in request.args:
            info_msg = {'Information': str('Request format is not valid. category-name and category-description must be passed')}
            return jsonify(info_msg)
        category_name=request.args.get('category-name')
        category_description=request.args.get('category-description')
        data=(category_name,category_description,)
        if category_name and category_description and request.method=='POST':
            sql_query="INSERT INTO ronwell_case_study.category_table(category_name,category_description) VALUES(%s,%s)"
            connection=mysql_object.connect()
            db_cursor=connection.cursor()
            db_cursor.execute(sql_query,data)
            connection.commit()
            logger.info("Just an information")
            response=jsonify('Category added successfully')
            response.status_code=200
            return response
        else:
            return abort(404)
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
        pass
        #db_cursor.close()
       #connection.close()


# GET all authors
# Example call format : curl http://127.0.0.1:5000/api/v1/authors
@app.route('/api/v1/authors/all')
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
# Example call format : curl http://127.0.0.1:5000/api/v1/blogs/all
@app.route('/api/v1/blogs/all')
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
    app.run(debug=True)