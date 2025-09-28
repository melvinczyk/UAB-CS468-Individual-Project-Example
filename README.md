# Project Example

### Get started

- Make a python virtual environment
- Download the requirements
- Run `python manage.py migrate`
- Run `python manage.py runserver`

## API Calling

**To Make Users**

Head to `127.0.0.1:8000/api/accounts/register/` and make a **POST** request:
  ```json
  {
    "username" : "name",
    "password" : "password",
  }
  ```
Response should be the username and password of the account.


**To Login**

Head to `127.0.0.1:8000/api/accounts/login/` and make a **POST** request:
```json
  {
    "username" : "name",
    "password" : "password",
  }
  ```
Response should be the refresh and access token.

**To Make a Task**

Head to `127.0.0.1:8000/api/tasks/` and include the access token as an authorization header. Make a **POST** request:
```json
  {
    "title" : "name",
    "due_date" : "YYYY-MM-DD",
  }
  ```
Response should be the database entry created for the task

**To View Tasks**

Head to `127.0.0.1:8000/api/tasks/` or `127.0.0.1:8000/api/tasks/<id_number>/`and include the access token as an authorization header. Make a **GET** request:

Response should be the listing of every task or the specific task with the id.
