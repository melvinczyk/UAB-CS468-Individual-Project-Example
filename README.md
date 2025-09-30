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


# What I am looking for

### Software Design / Modularity 

- Is your code organized in modules, does it separate concerns.
  - If someone were to look at your project design would they know what everything does?
- Are classes appropriate.
  - Do you have data classes that don't also deal with UI?
  - Are api classes aren't also manipulating the database, etc?
- Are files organized correctly.
  - Are your data classes stored in an appropriate folder?
  - Do you have folders organized or just a bunch of files in the main directory?
  - Is running your project simple and easy to do?

### Code Quality

- Is it readable?
  - I don't expect slop code.
  - Can I understand it.
- Is it **ALL** AI generated?
  - I want to see that you looked at the code and edited it, I do not want to see everything AI generated.
  - If I ask you what the code does, will you be able to tell me?

### APIs

- Are the endpoints structured correctly?
  - If you need to get data from an endpoint is the response appropriate?
  - Do HTTP requests make sense on endpoints?
    - Example: if you want to make a user do they make a request to `users/register`, and if you want to get a user do you make a GET to `users/`
    - Example: do not make a `POST` request if you are just querying the database.
    - Example: using `POST` for everything instead of propper `PUT`, `DELETE`, `PATCH`.
- Authentication
  - Is your authentication method **Industry Standard**, this is very wide but here is what I do not mean.
    - No plaintext passwords in a database, if you are going to do this **PLEASE HASH**
    - No logging in via a URL such as `/login?user=nick&pass=1234`
    - No hardcoded passwords
    - No client-side only authentication
    - No hidden form fields in your HTML or in Cookies
    - No IP-Based authentication
  - Does your authentication work, will I be able to access sensitive information if I make an unauthorized request to an endpoint.
- Correct responses and error handling for requests
  - If the request fails, return the error code and handle the error. In other words if it errors handle it and make sure it doesn't crash everything. ***I WILL TEST THIS***
  - It is best practice to check your status code of the request that comes back. Example: `if request.status_code == 200:` and making sure everything works when it doesn't.

### Frontend

- Does it look like you tried to make it look good
  - I am not expecting professional UI, but I want to see if you at least tried to make it look pretty.
- Login page
- Tasks
  - Can you make, view, and edit tasks all in the UI
  - Can you mark them as complete or not

### Database

- Is your database design make sense
  - Does it make sense on how you structured your data.
  - If you have multiple tables that are related, do they link up? Do they have a shared key? Do they have identification?
- Can you effectively read and write to the DB safely
  - If I make an API call will it wipe the database?
  - Can I have unauthenticated access to the database?
  - Can I access sensitive data when I am not supposed to?
  - Does reading only read and does writing only write to the correct values?

### Testing

- Do you have unit testing
  - I will **NOT** accept manual testing.
  - Do unit tests cover real testing. I don't want to see useless test that you put in just cause.
  - Do tests cover different aspects of your project. Does it cover APIs, databasing, authentication, etc
  - Do they all provide valid feedback, whether pass or fail
