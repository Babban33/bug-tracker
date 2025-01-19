<!-- ```bash
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

```bash
python manage.py makemigrations -->


# Setup

Install sqlite from here: [Website](https://www.sqlite.org/download.html).

Optionally to view database use [DB Browser](https://sqlitebrowser.org/dl/)

Clone repository:
```bash
git clone "https://github.com/Babban33/bug-tracker.git
```
Move inside cloned repo:
```bash
cd bug-tracker
```

Setup Virtual Environment:
```bash
python -m venv venv
venv\Scripts\activate
```

Create a superuser (Optional)
```bash
python manage.py createsuperuser
```

Run server
```bash
python manage.py runserver
```

That's it! Move to the [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and use it.