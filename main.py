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


# CRUD Operation - CREATE
@app.route('/add', methods=['POST'])
def add_book():
    try:
        json = request.json
        Book_name = json['book_name']
        Author_name = json['author_name']
        Publisher_name = json['publisher_name']
        if Book_name and Author_name and Publisher_name and request.method == 'POST':
            sql_query = "INSERT INTO books(Book_name, Author_name, Publisher_name) VALUES(%s, %s, %s)"
            data = (Book_name, Author_name, Publisher_name,)
            connection = mysql_object.connect()
            db_cursor = connection.cursor()
            db_cursor.execute(sql_query, data)
            connection.commit()
            response = jsonify('Book added!')
            response.status_code = 200
            return response
        else:
            abort(404)
    except Exception as e:
        print(e)
    finally:
        db_cursor.close()
        connection.close()

# CRUD Operation - READ
@app.route('/book/<int:id>')
def book(id):
    try:
        connection = mysql_object.connect()
        db_cursor = connection.cursor(pymysql.cursors.DictCursor)
        db_cursor.execute("SELECT * FROM books WHERE book_id=%s", id)
        record = db_cursor.fetchone()
        response = jsonify(record)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        db_cursor.close()
        connection.close()

# CRUD Operation - UPDATE
@app.route('/update', methods=['POST'])
def update_book():
    try:
        json = request.json
        id = json['id']
        Book_name = json['Book_name']
        Author_name = json['Author_name']
        Publisher_name = json['Publisher_name']
        if Book_name and Author_name and Publisher_name and id and request.method == 'POST':
            sql_query = "UPDATE books SET Book_name=%s, Author_name=%s, Publisher_name=%s WHERE book_id=%s"
            data = (Book_name, Author_name, Publisher_name, id,)
            connection = mysql_object.connect()
            db_cursor = connection.cursor()
            db_cursor.execute(sql_query, data)
            connection.commit()
            response = jsonify('Book updated!')
            response.status_code = 200
            return response
        else:
            abort(404)
    except Exception as e:
        print(e)
    finally:
        db_cursor.close()
        connection.close()

# CRUD Operation - DELETE
@app.route('/delete/<int:id>')
def delete_book(id):
    try:
        connection = mysql_object.connect()
        Pointer = connection.cursor()
        Pointer.execute("DELETE FROM books WHERE book_id=%s", (id,))
        connection.commit()
        response = jsonify('book deleted!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()


if __name__ == "__main__":
    app.run()