# Python Flask REST API + MYSQL

In this repository we will create a REST API with Flask microframework and data provided from MySQL Database.
Database and tables already created therefore we are not creating by code.

## INSTALLATION

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages/libraries.

```bash
pip install requirements.txt
```

## USAGE
First of all you must go from terminal to project directory. After you moved into project directory run main.py file from command line and you are ready for api calls
```bash
cd project_directory 
python main.py
```

GET all categories 
```bash
curl http://127.0.0.1:5000/api/v1/categories
```
GET category details by category name
```bash
curl http://127.0.0.1:5000/api/v1/categories?category-name=Horrors
```
parameter_name | parameter_type 
--- | --- | 
category-name | string

POST category
```bash
http://127.0.0.1:5000/api/v1/categories/post?category-name=FR&category-description=FR
```
parameter_name | parameter_type 
--- | --- | 
category-name | string 
category-description | string

GET all authors
```bash
curl http://127.0.0.1:5000/api/v1/authors
```

POST author
```bash
http://127.0.0.1:5000/api/v1/authors/post?first-name=Hasan&last-name=Digital
```
parameter_name | parameter_type 
--- | --- | 
first-name | string 
last-name | string

GET all blogs 
```bash
curl http://127.0.0.1:5000/api/v1/blogs/all
```
POST blogs
```bash
http://127.0.0.1:5000/api/v1/blogs/post?blog-title=Euro&blog-content=Euro&image-path=yuru.com&blog-tags=ekonomi&blog-category-id=1&blog-author-id=1
```
parameter_name | parameter_type 
--- | --- | 
blog-title | string 
blog-content | string
image-path | string 
blog-tags | string
blog-category-id | string 
blog-author-id | string

## CONTRIBUTING
Pull requests are welcome. 

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## LICENSE
[UNLICENSE](https://choosealicense.com/licenses/unlicense/)