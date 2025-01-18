```bash
python -m venv venv
venv\Scripts\activate
pip install django matplotlib
django-admin startproject bug_tracker .

python manage.py startapp bugs
python manage.py startapp users

#This will print secret key
python
import secrets
print(secrets.token_urlsafe(50))

pip install python-dotenv
```

create a .env file in root and add the printed key in the file


update the settings.py with custom user model, email backend, dirs.

