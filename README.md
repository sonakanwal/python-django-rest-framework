# Python Training - Django Rest Framework
This repository contains all project files for python training project with REST APIs on Django REST Framework

# Requirements
  - Python
  - Django 
  - Django REST Framework
  - Django REST Framework JWT 

# 1. Create Virtual Environment
      pip install virtualenv

# 2. Activate Your Environment
      .\Scripts\activate
     
# 3. Installation
     pip install -r requirements.text

# 4. Migrate
     - Create migrations for your models
        python manage.py makemigrations
     
     - Apply Migrations
       python manage.py migrate

# 4. Usage
     Use following Endpoint to access login view and obtain the JWT token: 
     http://localhost:8000/api/auth/login/
     
     Use following Endpoint to create articles, append Authorization Header with the Bearer Token obtained from above URL: 
     http://localhost:8000/api/create_article/
     
     Use following Endpoint to get articles list without authentication: 
     http://localhost:8000/api/articles/
     
     Use following Endpoint to get article by id, put and delete. Append Authorization Header with the Bearer Token obtained from above      URL:
     http://localhost:8000/api/articles/id/
     
     Also, find following URLs for JWT tokens:
      -Get Access Token: 
       http://localhost:8000/auth-jwt/

      -Refresh Token: 
       http://localhost:8000/auth-jwt-refresh/

      -Verify Token:
       http://localhost:8000/api/auth-jwt-verify/
     
