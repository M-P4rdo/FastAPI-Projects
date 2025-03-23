# 🚀 Product Management with FastAPI

This project is a REST API for product management, implemented with **FastAPI** and **MongoDB**. It includes Product CRUD.

## Technologies used

- **FastAPI** - Modern and fast web framework.
- **MongoDB** - NoSQL database
- **Motor** - Asynchronous client for MongoDB
- **Pydantic** - Data validation


## Installation

### Clone repository
git clone --single-branch --branch Product_Management_Mongo https://github.com/M-P4rdo/FastAPI-Projects.git  
cd FastAPI-Projects.git

### Create a virtual environment and install dependencies
Create virtual environment (.venv)  
Activate virtual environment

### Install dependencies
pip install -r requirements.txt 


## Database Configuration

### **1. Create a '.env' file in the root of the project with the following structure**  
MONGO_URL=mongodb://localhost:27017
DB_NAME=product_management 

### **2. Start MongoDB**  
Open the Command Prompt terminal and run (mongod)
Open a new Command Prompt terminal and run (mongosh)

### **3. (Optional) Insert test products**  
python seed.py  


## 🚀 Execute the API  
uvicorn app.main:app --reload  
The API will be available in **'http://127.0.0.1:8000'**.


## Main Endpoints  

### **Products**
| Method | Endpoint       | Description            |
|--------|----------------|------------------------|
| 'POST' | '/products/'      | Create a new product     |
| 'GET'  | '/products/'      | List products            |   
| 'GET'  | '/products/{id}'  | Get a product by ID      |
| 'PUT'  | '/products/{id}'  | Update a product         |
| 'DELETE' | '/products/{id}' | Delete a product        | 


## Testing at Postman

### User Endpoints 
  
**Create User**  
**Method:** 'POST'  
**URL:** 'http://127.0.0.1:8000/products/'  
**Body (raw):** JSON  
{  
  "name": "-----",  
  "price": -----,  
  "category": "-----",  
  "description": "-----"  
}  

**List Users**  
**Method:** 'GET' **URL:** 'http://127.0.0.1:8000/products/'  
  
**Get User by ID**  
**Method:** 'GET' **URL:** 'http://127.0.0.1:8000/products/{product_id}'   

**Delete User**  
**Method:** 'DELETE' **URL:** 'http://127.0.0.1:8000/products/{product_id}'  

**Update User**  
**Method:** 'PUT' **URL:** 'http://127.0.0.1:8000/products/{product_id}'  
**Body (raw):** JSON  
{  
  "name": "-----",  
  "price": -----,  
  "category": "-----",  
  "description": "-----"  
}  

**The interactive API documentation is available at**  
'http://127.0.0.1:8000/docs' (Swagger UI)   
'http://127.0.0.1:8000/redoc' (ReDoc)  