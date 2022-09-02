# Book Library
A book library built with Python (Django and Django Rest Framework).

<br>

## Endpoints
- GET `/books/` - Returns a list of books in the database in JSON format
- GET `/book/{{id}}/` - Returns a detail view of the specified book id. Nest author
details in JSON format
- GET `/authors/` - Returns a list of authors in the database in JSON format
- GET `/author/{{id}}/` - Returns a detail view of the specified author id
- POST `/author/` - Creates a new author with the specified details - Expects a JSON
body
- POST `/book/` - Creates a new book with the specified details - Expects a JSON body
- PUT `/author/{{id}}/` - Updates an existing author - Expects a JSON body
- PUT `/book/{{id}}/` - Updates an existing book - Expects a JSON body

<br>

To get it running on your local machine, follow the steps below:

1. Run the commands below in your terminal:

```
git clone git@github.com:israelabraham/book-library.git
```

2. Change directory to book-library:

```
cd book-library
```

3. Install the requirements with the command below:

```
pipenv install -r requirements.txt
```

4. Run the development server with

```
python manage.py runserver
```

5. Launch your browser and navigate to:

```
http://127.0.0.1:8000
```

<br>

## Screenshot


