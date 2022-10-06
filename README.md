# NutritionistsHelper

## Tech Stack
1. Python 3.9.13
2. Django 4.1.2
3. Django Rest Framework
4. SQLite

## Setup
1. Install python 3.9.13 on the system.
2. Install dependencies using
```bash
pip install -r requirements.txt
```
3. Migrate database changes using
```bash
python manage.py migrate
```
4. Create an admin user for accessing admin panel using
```bash
python manage.py createsuperuser
```
5. Run application on port 8000 using
```bash
python manage.py runserver
```

## API Endpoints

### Accounts
___
#### ROUTE : `api/v1/accounts/login`  
REQUEST : **POST**  
PARAMS : *username*, *password*  
RESPONSE : ***Access Token***, ***Refresh Token*** 

#### ROUTE : `api/v1/accounts/token/refresh/`  
REQUEST : **POST**  
PARAMS : *refresh*  
RESPONSE : ***Access Token*** 

### Recipe
___
#### ROUTE : `api/v1/recipe/`  
AUTH : **Bearer token**  
REQUEST : **GET**  
PARAMS : *None*  
RESPONSE : ***List of recipes (either created by user or assigned to user)***

#### ROUTE : `api/v1/recipe/<pk>`  
AUTH : **Bearer token**  
REQUEST : **GET**  
PARAMS : *None*  
ARGS : portion  
RESPONSE : ***Recipe details (either created by user or assigned to user)***
EXPLANATION: <pk> is primary key of a particular recipe.  
###### Example
1. api/v1/recipe/1
2. api/v1/recipe/1?portion=0.5

## Files related to task
### Task 3
1. accounts/models
2. recipe/models
### Task 4
1. recipe/views

## Format for ingredients and instructions

### Ingredient field Format:
    {
        "ingredients": [
            { "name" : "ingredient_name",
              "quantity" : ingredient_quantity
            }
        ]
    }
#### Example:

    {
        "ingredients": [
            {"name": "tomato", "quantity": 12},
            {"name": "carrot", "quantity": 5}
        ]
    }

### Instruction field Format:
    {
        "instructions": [
            "Instruction 1",
            "Instruction 2"
        ]
    }
#### Example:

    {
        "instructions": [
            "Cut vegetables",
            "Add salt"
        ]
    }

### Create Recipe
1. Login to admin panel by visiting `localhost:8000/admin` and using credentials you added in step 4.
2. Add Recipes by clicking on recipe in admin panel and then on Add Recipe button on top right. (Format and sample for both ingredient and instruction field are given below)
3. Add Nutritionist by clicking on Nutritionist and then on ADD NUTRITIONIST on top right.
4. Add recipes to Nutritionist during registration process.
5. Add Customer by clicking on Nutritionist and then on ADD NUTRITIONIST on top right.
6. Add recipes to Customer during registration process.