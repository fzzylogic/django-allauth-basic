# django-allauth-basic

This has some basic config for django-allauth and includes django-allauth-ui for prettier sign-in form styling.

## Quickstart

    git clone <project>
    cd <project>
    python -m venv lenv       # or e.g. wenv on windows
    source lenv/bin/activate  # or just wenv\Scripts\activate on windows
    python -m pip install --upgrade pip setuptools
    pip install -r requirements.txt
    cd mysite
    python manage.py runserver

Visit localhost:8000/accounts/login
