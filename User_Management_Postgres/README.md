# 🚀 User Management with FastAPI

This project is a REST API for user management, implemented with **FastAPI**, JWT authentication and **PostgreSQL**. It includes user CRUD and secure authentication with JWT tokens.

## Technologies used

- **FastAPI** - Modern and fast web framework.
- **PostgreSQL** - Relational database.
- **SQLAlchemy** - ORM to interact with PostgreSQL.
- **Alembic** - Database migrations.
- **JWT (JSON Web Tokens)** - For secure authentication.
- **bcrypt** - Password cracking.


## Installation

### Clone repository
git clone --single-branch --branch User_Management_Postgres https://github.com/M-P4rdo/FastAPI-Projects.git  
cd FastAPI-Projects.git

### Create a virtual environment and install dependencies
Create virtual environment (.venv)  
Activate virtual environment

### Install dependencies
pip install -r requirements.txt  
pip install --upgrade passlib


## Database Configuration

### **1. Create a '.env' file in the root of the project with the following structure**  
DATABASE_URL=postgresql://user:password@localhost/nombre_db  
SECRET_KEY=your_secret_key  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=30  

### **2. Execute database migrations**  
alembic revision --autogenerate -m "create users table"   
alembic upgrade head 

Open the alembic.ini file and edit the line:  
(sqlalchemy.url) = postgresql://user:password@localhost/db_name

### **3. (Optional) Insert test users**  
python seed.py  


## 🚀 Execute the API  
uvicorn app.main:app --reload  
The API will be available in **'http://127.0.0.1:8000'**.


## Main Endpoints  

### Authentication
| Method | Endpoint       | Description                |
|--------|----------------|----------------------------|
| 'POST' | '/auth/login'  | Log in and get JWT token   |

### **Usuarios**
| Method | Endpoint       | Description            |
|--------|----------------|------------------------|
| 'POST' | '/users/'      | Create a new user      |
| 'GET'  | '/users/'      | List users (requires authentication)      |   
| 'GET'  | '/users/{id}'  | Get a user by ID (requires authentication)|
| 'PUT'  | '/users/{id}'  | Update a user (requires authentication)   |
| 'DELETE' | '/users/{id}' | Delete a user (requires authentication)  | 


## Testing at Postman

### Get Authentication Token  
**Create User**  
**Method:** 'POST'  
**URL:** 'http://localhost:8000/users/'  
**Body (raw):** JSON  
{  
  "username": "-----",  
  "email": "-----@example.com",  
  "password": "-----"  
} 

**Method:** 'POST'  
**URL:** 'http://localhost:8000/auth/login'   
**Body (raw):** JSON  
{  
  "email": "-----",  
  "password": "-----"  
}  
**Save the Token** for future requests.   

### User Endpoints  
**Add 'Authorization: Bearer <TOKEN>' in the protected requests.**  

**List Users**  
**Method:** 'GET' **URL:** 'http://localhost:8000/users/'  

**Get User by ID**  
**Method:** 'GET' **URL:** 'http://localhost:8000/users/{user_id}'   

**Delete User**  
**Method:** 'DELETE' **URL:** 'http://localhost:8000/users/{user_id}'  

**Update User**  
**Method:** 'PUT' **URL:** 'http://localhost:8000/users/{username}'  
**Body (raw):** JSON  
{  
  "username": "-----",  
  "email": "-----@example.com",  
  "password": "-----"  
}  

**The interactive API documentation is available at**  
'http://127.0.0.1:8000/docs' (Swagger UI)   
'http://127.0.0.1:8000/redoc' (ReDoc)  

