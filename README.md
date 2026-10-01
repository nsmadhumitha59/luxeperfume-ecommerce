# LUXEPERFUME

A Django fragrance shop with product browsing, product details, a session-based cart, checkout, and informational pages.

## Requirements

- Python 3.10 or newer
- Django 5.2.17

## Setup

Run these commands from the repository root in PowerShell:

```powershell
cd .\fragrance_store
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "Django==5.2.17"
python manage.py migrate
```

The project uses SQLite for local development. The database file is created locally and is excluded from Git.

Set a local Django secret key before starting the server:

```powershell
$env:DJANGO_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(50))"
```

`DJANGO_DEBUG` defaults to `True` for local development. Do not use the development fallback secret or `DEBUG=True` in production.

## Run

```powershell
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. To add or edit products, create an admin account with `python manage.py createsuperuser` and use <http://127.0.0.1:8000/admin/>.

## Main Pages

- `/` - Home
- `/products/` - Shop
- `/product/<id>/` - Product details
- `/cart/` - Shopping cart
- `/checkout/` - Checkout
- `/about/` - About
- `/contact/` - Contact

## Project Layout

- `fragrance_store/` - Django project, app, templates, migrations, and product images
- `shop/static/shop/` - Shared CSS and JavaScript assets
- `.gitignore` - Excludes local databases, environment files, and generated files

## Checks

```powershell
python manage.py check
```