# Book Library
A book library built with Python (Django and Django Rest Framework).

## Frontend
![book-library](https://user-images.githubusercontent.com/55067204/188288090-7020fb1e-dc56-4f54-833f-afeb0a36583b.png)

Find the frontend repository [here](https://github.com/israelabraham/book-library-frontend)

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
git clone git@github.com:israelabraham/book-library-backend.git
```

2. Change directory to book-library-backend:

```
cd book-library-backend
```

3. Install the requirements with the command below:

```
pipenv install -r requirements.txt
```

4. Run the test cases with
```
python manage.py test
```

5. Run the development server with

```
python manage.py runserver
```

6. Launch your browser and navigate to:

```
http://127.0.0.1:8000
```

<br>

## Screenshot

![book-library-api-docs](https://user-images.githubusercontent.com/55067204/188197501-0683b463-5879-4661-aa66-42811c96d0cf.png)

