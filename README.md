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

## Software Design & Modularity 

- **Project organization**  
  - Clear separation of concerns
  - If someone were to look at your project design would they know what everything does?
- **Class usage**
  - Are classes used effectively, examples:
  - Data classes ≠ UI logic  
  - API classes ≠ database manipulation
- **File/folder structure**  
  - Data classes in the right place  
  - Organized folders (not a cluttered root directory)  
  - Is running your project simple and easy to do?

---

## Code Quality

- **Readability**  
  - Code should be clean and understandable  
  - No slop code
- **Original work**  
  - Not entirely AI-generated  
  - You should be able to explain your own code  

---

## APIs

- **Endpoints**  
  - Proper REST conventions (GET, POST, PUT, DELETE, PATCH)  
  - Example:  
    - Create user → `POST /users/register`  
    - Fetch user → `GET /users/`  
    - Don’t use `POST` for simple queries or incorrect usage if you can use `PATCH`, `DELETE`, `PUT`, `GET`, etc.
- **Authentication (industry standard required)**
  - Is your authentication method **Industry Standard**, this is very broad but here is what I do **not** mean.
    - No plaintext passwords in a database, if you are going to do this **PLEASE HASH**
    - No logging in via a URL such as `/login?user=nick&pass=1234`
    - No hardcoded passwords
    - No client-side only authentication
    - No hidden form fields in your HTML or in Cookies
    - No IP-Based authentication
- **Error handling**  
  - Return meaningful status codes  
  - Handle failures gracefully (**no crashes**)  
  - Always check status codes (e.g. `if response.status_code == 200:`)  

---

## Security ( I will be THOROUGHLY trying to break your project)
- **Unauthorized access / access control**
  - Can I make unauthorized API requests?
  - Can users view or modify other users' tasks/data?
  - Are role/permission checks enforced server-side?
 
- **Input validation & injections**
  - Do you validate responses and data server-side?
  - Can I make an SQL injection attack on your database?
  - No unsafe string concatenation for DB queries or shell commands.
 
- **Authentication robustness**
  - Are paswords stored **hashed**?
  - Are tokens/sessions protected (no hardcoded secrets, no login via URL, etc.)?
 
---

## Frontend

- **Effort matters** — doesn’t need to be professional, but show care and effort in your design 
- **Login page**  
- **Tasks management**  
  - Create / View / Edit tasks  
  - Mark complete or incomplete

---

## Database

- **Schema design**  
  - Logical structure and relationships  
  - Proper keys / identifiers in relational models  
- **Data safety**  
  - No accidental wipes via API  
  - No unauthenticated or unauthorized DB access  
  - Reads = read only, Writes = update correct values only
 
---

## Testing

- **Unit tests required** (manual testing will not be accepted)  
- **Meaningful coverage**  
  - APIs  
  - Database  
  - Authentication
  - etc.
- **No filler tests** 
  - No filler or useless tests
  - Tests must give usefull feedback
- **Clear results** whether pass or fail  
