# quillapi (Flask API Foundation for Notes / Quill Blogs)

![Python](https://img.shields.io/badge/Python-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2F2F2F?logo=flask&logoColor=white)
![Bcrypt](https://img.shields.io/badge/Bcrypt-Encryption-blue?logo=flask&logoColor=white)
![JWT Extended](https://img.shields.io/badge/JWT_Extended-Auth-4169E1?logo=flask&logoColor=white)
![Migrate](https://img.shields.io/badge/Migrate-DB--Migrations-red?logo=flask&logoColor=white)
![Smorest](https://img.shields.io/badge/Smorest-API-2E8B57?logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-32CD32?logo=flask&logoColor=white)
![marshmallow](https://img.shields.io/badge/marshmallow-Schema-orange?logo=python&logoColor=white)

```bash
pip install Flask Flask-Bcrypt Flask-JWT-Extended Flask-Migrate Flask-Smorest SQLAlchemy marshmallow python-dotenv
```

## 📌 Overview

A RESTful API built using **Flask-Smorest**, **Flask-SQLAlchemy**, and **Marshmallow** for managing user accounts and storing associated *quills* (custom content). This project provides a modular and scalable backend solution suitable for content-driven applications.


## 🚀 Features

- RESTful API endpoints
- Authentication support: JWT
- Database integration: Postgres
- Automatic API documentation: Swagger/OpenAPI 3.0.3

## 🛠 Tech Stack

- Python >= 3.10
- Flask_smorest
- Flask_SQLAlchemy/ORM
- Marshmallow (for request/response schemas)
- flask_jwt_extended : access and refresh 
- psycopg2-binary (PostgreSQL driver)
## 📦 Installation

Follow these steps to set up and run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/rozercode/quillapi.git
cd quillapi
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. set config database url according your environment 
- you need to manually make database. <database_name>
```bash
SQLALCHEMY_DATABASE_URI = "postgresql://<database_username>:<password>@localhost/<database_name>"
```

### 5. Initialize the database (make sure postgres server is running)
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 6. execute run.py file
```bash
python run.py
# for linux ubuntu,linux mint : python3 run.py
```
your api is running at http://localhost:5000/






