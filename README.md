# Purbeurre
App built for project 8 in Python developer path at Openclassrooms.

The startup Pur Beurre wants to develop a web platform for its customers. This site will allow anyone to find a healthy substitute for a food considered "Too fat, too sweet, too salty".

## Online application

## Requirements
* Python 3
* Django
* Psycopg2
* PostgreSql
* Requests
* Pillow

## Setup
To run this application locally:

* Create a virtual environment. First, install pipenv:
    ```
    pip install --user pipenv
    ```

* Clone / create the application repository:
    ```
    git clone https://github.com/etiennody/purbeurre.git && cd purbeure_project 
    ````

* Install the requirements:
    ```
    pipenv install
    ```

* Activate the pipenv shell:
    ```
    pipenv shell
    ```

* Create a database with postgresql:
    Add and update this information in environment variables file named .env in root directory:
    * PURBEURRE_DBNAME=<your purbeurre_dbname>
    * PURBEURRE_DBUSER=<your purbeurre_dbuser>
    * PURBEURRE_DBPASSWD=<your purbeurre_dbpassword>

* Import data from Openfood Facts:
    ```
    python manage.py import_off
    ```

* Run the GrandPy Bot application:
    ````
    python manage.py runserver

    ````

* Launch Django server:
You can visit localhost at https://127.0.0.1:8000/

* Enjoy!