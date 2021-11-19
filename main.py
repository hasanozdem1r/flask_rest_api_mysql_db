import pymysql
from database_config import mysql_object,create_record,connect_db
from app import app
from flask import Flask, jsonify, request,abort
from datetime import datetime


# CATEGORY CRUD OPERATIONS

# GET all categories
# Example call format : curl http://127.0.0.1:5000/api/v1/categories/all
@app.route('/api/v1/categories/all')
def show_all_categories():
    try:
        connection, db_cursor = connect_db()
        db_cursor.execute("SELECT * FROM ronwell_case_study.category_table")
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
# Example call format : curl http://127.0.0.1:5000/api/v1/categories?category-name=Horror
@app.route('/api/v1/categories')
def show_category():
    try:
        if 'category-name' in request.args:
            category_name:str=str(request.args.get('category-name'))
            connection, db_cursor = connect_db()
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

# POST category (create new category)
#In postman select post method -> http://127.0.0.1:5000/api/v1/categories/post?category-name=FR&category-description=FR
@app.route('/api/v1/categories/post',methods=['POST'])
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
            db_cursor,connection=create_record(sql_query,data)
            response=jsonify('Category added successfully')
            response.status_code=200
            return response
        else:
            return abort(404)
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
       db_cursor.close()
       connection.close()

# AUTHOR CRUD OPERATIONS

# GET all authors
# Example call format : curl http://127.0.0.1:5000/api/v1/authors/all
@app.route('/api/v1/authors/all')
def show_all_authors():
    try:
        connection, db_cursor = connect_db()
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

# POST authors (create new author)
# In postman select post method -> http://127.0.0.1:5000/api/v1/authors/post?first-name=Hasan&last-name=Digital
# date passed automatically from datetime.now()
# We assume that if author is added new he/she doesn't have any blog which is added
@app.route('/api/v1/authors/post',methods=['POST'])
def add_author():
    try:
        if not 'first-name' in request.args or not 'last-name' in request.args:
            info_msg = {'Information': str('Request format is not valid. first-name and last-name must be passed')}
            return jsonify(info_msg)
        first_name=request.args.get('first-name')
        last_name=request.args.get('last-name')
        date_joined=datetime.now()
        data=(first_name,last_name,0,str(date_joined.strftime('%Y-%m-%d %H:%M:%S')),)
        if first_name and last_name and request.method=='POST':
            sql_query='INSERT INTO ronwell_case_study.author_table (first_name,last_name,blog_amount,date_joined) VALUES(%s,%s,%s,%s)'
            db_cursor, connection = create_record(sql_query, data)
            response = jsonify('Author added successfully')
            response.status_code = 200
            return response
        else:
            return abort(404)
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
         db_cursor.close()
         connection.close()

# BLOG CRUD OPERATIONS

# GET all blogs
# Example call format : curl http://127.0.0.1:5000/api/v1/blogs/all
@app.route('/api/v1/blogs/all')
def show_all_blogs():
    try:
        connection, db_cursor = connect_db()
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

# POST blogs
# In postman select post method -> http://127.0.0.1:5000/api/v1/blogs/post?blog-title=DollarMı&blog-content=Dollmaz&image-path=dolmaz.com&blog-tags=ekonomi&blog-category-id=1&blog-author-id=1
# 2nd example call -> http://127.0.0.1:5000/api/v1/blogs/post?blog-title=Euro&blog-content=EuroooooooooooooooooooBe&image-path=yuru.com&blog-tags=ekonomi&blog-category-id=1&blog-author-id=1
@app.route('/api/v1/blogs/post',methods=['POST'])
def add_blog():
    try:
        if not 'blog-title' in request.args or not 'blog-content' in request.args or not 'image-path' in request.args or not 'blog-tags' in request.args \
                or not 'blog-category-id' in request.args or not 'blog-author-id' in request.args :
            info_msg = {'Information': str('Request format is not valid. Pass arguments correctly must be passed')}
            return jsonify(info_msg)
        blog_title=request.args.get('blog-title')
        blog_content=request.args.get('blog-content')
        image_path=request.args.get('image-path')
        blog_tags=request.args.get('blog-tags')
        blog_category_id=int(request.args.get('blog-category-id'))
        blog_author_id=int(request.args.get('blog-author-id'))
        data_created = datetime.now()
        #data = (first_name, last_name, 0, str(date_joined.strftime('%Y-%m-%d %H:%M:%S')),)
        if blog_title and blog_content and image_path and blog_tags and blog_category_id and blog_author_id and request.method=='POST':
            # check given category is existed or not
            sql_query="SELECT COUNT(first_name) FROM ronwell_case_study.author_table where author_id=%s"
            connection = mysql_object.connect()
            db_cursor = connection.cursor()
            db_cursor.execute(sql_query,(blog_author_id,))
            size_author=int(db_cursor.fetchall()[0][0])
            sql_query = "SELECT COUNT(category_name) FROM ronwell_case_study.category_table where category_id=%s"
            db_cursor.execute(sql_query,(blog_category_id,))
            size_category =int(db_cursor.fetchall()[0][0])
            # if size is 0 author or category is not existed therefore user cannot add blog
            if size_author==0 or size_category==0:
                message_dict = {'Information': str('Author or category is not valid. Blog cannot be added')}
                return jsonify(message_dict)
            else:
                # insert blog to table
                sql_query="INSERT INTO ronwell_case_study.blog_table (blog_title,blog_content,date_created,blog_image_link,blog_tags,blog_category_id,blog_author_id) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                data=(blog_title,blog_content,str(data_created.strftime('%Y-%m-%d %H:%M:%S')),image_path,blog_tags,blog_category_id,blog_author_id,)
                db_cursor, connection=create_record(sql_query, data)
                # get current author number of blog
                sql_query='SELECT COUNT(blog_title) FROM ronwell_case_study.blog_table where blog_author_id=%s'
                db_cursor.execute(sql_query, (blog_author_id,))
                amount_blog = int(db_cursor.fetchall()[0][0])
                # update author table blog_amount field
                sql_query='UPDATE ronwell_case_study.author_table SET blog_amount=%s WHERE author_id=%s'
                db_cursor.execute(sql_query,(amount_blog,blog_author_id,))
                connection.commit()
                response = jsonify('Blog added successfully')
                response.status_code = 200
                return response
    except Exception as error:
        error_dict={'Error':str(error)}
        return jsonify(error_dict)
    finally:
         db_cursor.close()
         connection.close()
if __name__ == "__main__":
    app.run(debug=True)