# Creating React Project using Vite

1. npm create vite@latest
2. Provide the project name
3. Select language : TypeScript
4. Got into the project directory and install dependencies

# Creating Django project

1. make django project : django-admin startproject backend
2. to start an app : python manage.py startapp <api name>
3. to run server : python manage.py runserver
4. to make migrations : python manage.py makemigrations
5. to migrate : python manage.py migrate

# Setting up venv

1. python -m venv env
2. source env/bin/activate

# Extra commands

1. pip install -r requirements.txt
2. python -c "import sys; print(sys.executable)" to check the path of the python

# Deploying commands on Choreo

# Notes

- Use django to return data not html
-

# Django Course Notes

1. views.py : its used as a request handler ; given a request it returns a response
2. models.py : creating the data models for the storing the data
3. Three fields for identifying the type of object in other app models.py :
   1. content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   2. object_id = models.PositiveIntegerField()
   3. content_object = GenericForeignKey()
4. Meta to add additional information to the models class like name and indices
5. query_set types for lookup = https://docs.djangoproject.com/en/5.0/ref/models/querysets/
6. for field types in creating models : https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types
7. Q objects for or queries from data model
8. Serializer : converts a model instance to a dictionary 
9. Serializer fields : https://www.django-rest-framework.org/api-guide/fields/
10. HTTP status : https://httpstatuses.io/

