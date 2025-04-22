
# Django Rest Inventory Apps

Django REST Framework (DRF)-based API for CRUD operation, Multiparse Json and File Field and Logger.

## 🔗 Table of content


- [Features](#Features)

- [Tech Stack](#TechStack)

- [Environment Variables](#EnvironmentVariables)

- [Installation](#Installation)

- [Usage/Examples](#Usage/Examples)

- [Screenshots](#Screenshots)

- [License](#License)


## 🔗 Features

✅ API create inventory

✅ API list inventory

✅ API detail inventory

✅ API update inventory

✅ API delete inventory

✅ Logging Request and Response
## 🔗 Tech Stack

**Backend:**
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

**Database:**
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)


## 🔗 Environment Variables

To run this project, you will need to add the following environment variables to your .env file inside inventory_apps

```
SECRET_KEY='django-insecure-fveqqscok$tm-hk6w)xf7k(yyx35vix)%b8388h8el^scs6f63'
DEBUG = 'True'
DB_NAME = inventory
DB_USER = postgres
DB_PASSWORD = postgres
DB_HOST = localhost
DB_PORT = 5432
SUPER_USER = admin
SUPER_EMAIL = admin@inventory.com
SUPER_PASS = password2025
SIGNING_KEY = Thequickbrownfoxjumpsoverthelazydog
```

## 🔗 Installation

🔹 Prerequisites
Ensure you have the following installed:

    Python (3.13)

    Git

    PostgresSQL

    Postman


🔹 Clone the Repository
```bash
git clone https://github.com/FarizAfkar/django-rest-inventory-apps.git
```

🔹 Create a Virtual Environment
```bash
python -m venv env
Windows: venv\Scripts\activate
```

🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

🔹 Apply Migrations
```bash
cd inventory_apps
python manage.py makemigrations
python manage.py migrate
```

🔹 Start the Development Server
```bash
python manage.py runserver
```

Now, open http://127.0.0.1:8000/swagger/ in your browser.

OR

In potsman press [ctrl + O], then drop or select file. choose `Inventory.postman_collection.json`. Already provide in Repository.
## 🔗 Usage/Examples

🔹 Authentication with JWT

    in postman navigate to Token folder.

    1. Choose Obtain Token.
    2. In body section choose raw and type

        {
	        "username": "admin",
            "password": "password2025"
        }
    3. Response will
        {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTQwMTcyNiwiaWF0IjoxNzQ1MzE1MzI2LCJqdGkiOiJlNjQ3NmJiYmIxMmQ0NWEwYjA4MjQ5ZDAxYzUwMGQ4MyIsInVzZXJfaWQiOjF9.ZWZTHnfU8Dq5mfqO4V3r5-koM9HNobhT0LUaOaSmhOs",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MzU4NTI2LCJpYXQiOjE3NDUzMTUzMjYsImp0aSI6ImI4ZGYxNmY0MWY4OTQyMWQ4NTU5ZGQ2YTNkNTZkYmNjIiwidXNlcl9pZCI6MX0.iEiAZxRx_la_GzSMucSoV9D_J92BE9BuigalRIGqB6k"
        }

    4. Copy the access Response. For each Method Get, Post, etc navigate to Authorization. in Auth Type choose Bearer Token and Paste the access Response


🔹 Create inventory

    1. Go/navigate to [POST] Post data > Body > Form-data

    2. Fill the name, quantity, serial_number, additional_info, image, created_by

    3. Click Send


🔹 List inventory

    1. Go/navigate to [Get] Get list data

    2. Click Send


🔹 Detail inventory

    1. Go/navigate to [Get] Get detail data

    2. {{base_url}}inventory/detail/{id}/ change the {id} to 1 or 2

    3. Click Send


🔹 Update inventory

    1. Go/navigate to [PUT] Update data > Body > Form-data

    2. {{base_url}}inventory/detail/{id}/ change the {id} to 1 or 2

    3. Fill the name, quantity, serial_number, additional_info, image, updated_by

    4. Click Send


🔹 delete inventory

    1. Go/navigate to [DEL] Delete data

    2. {{base_url}}inventory/detail/{id}/ change the {id} to 1 or 2

    3. Click Send


## 🔗 Screenshots

![Screenshot 2025-04-22 175508](https://github.com/user-attachments/assets/9e46c093-57f9-4d04-8fec-80f8a4288863)

![Screenshot 2025-04-22 175547](https://github.com/user-attachments/assets/91bdb41b-f187-41a2-800a-8d28336ca61b)

![Screenshot 2025-04-22 175622](https://github.com/user-attachments/assets/ef79573c-c93f-4d52-8333-25ad252ef07f)

![Screenshot 2025-04-22 175659](https://github.com/user-attachments/assets/26468a71-951a-466b-aed7-adc433dfa5d5)


## 🔗 License

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)]((https://choosealicense.com/licenses/mit/))

## 🔗 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-FarizAfkar-blue?logo=linkedin)](https://www.linkedin.com/in/farizafkar/)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-red?logo=gmail)](mailto:high.oc7ane@gmail.com)
