

# Social login System

Social login System is a web application that allows users to sign in with Facebook/Google social site along with that get all users information/Current login users.
Basically, the user authentication is done by using token using django-rest-framework-social-oauth2 package.

This project contains the Django back-end with Django REST framework and back-end code required to make it all work.



## Django setup instructions.



1. Create a python virtual environment using below command.

   `python3 -m venv virtual-env`

2. Activate the environment.

   `source virtual-env/bin/activate`

3. Install dependencies.

   `pip install -r requirements.txt`

4. You can set the SOCIAL_AUTH_FACEBOOK_KEY,SOCIAL_AUTH_FACEBOOK_SECRET/GOOGLE_OAUTH2_KEY,GOOGLE_OAUTH2_SECRET  settings in `settings.py`

5. If you are using a fresh database in local execute this commands.

   `python manage.py makemigrations `

   `python manage.py migrate`

6. Run this command and your django app should be running on port `8000`

   `python manage.py runserver`
