# Django Admin Soft Dashboard

Modern template for **Django Admin Interface** coded on top of **[Soft UI Dashboard](https://github.com/app-generator/ct-soft-ui-dashboard-enh)** (free version). 

> UI Kit: [Soft UI Dashboard](https://github.com/app-generator/ct-soft-ui-dashboard-enh) **v1.0.6-enh1**

<br>

## **Links & Resources**

- 👉 [Soft UI Dashboard Django](https://appseed.us/product/soft-ui-dashboard/django/) - `free starter` that uses the same UI Kit
- 👉 [Soft UI Dashboard Django](https://django-soft-ui-dashboard.appseed-srv1.com/) - `LIVE Demo`
- 👉 More [Django Dashboards](https://appseed.us/admin-dashboards/django) provided by AppSeed 

<br />

## Why Django Admin Soft?

- Bootstrap 5 Design: **Soft UI Dashboard** (Free version) provided by **Creative-Tim**
- New fresh look
- Responsive mobile interface
- Useful admin home page
- Minimal template overriding
- Easy integration

<br />

![Django Admin Soft - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192209346-32d797c6-71b2-4b15-9910-a05af3ce4f86.jpg)

<br>

## How to use it

<br />

> 👉 Install the package via `PIP` 

```bash
$ pip install django-admin-soft-dashboard
// OR
$ pip install git+https://github.com/app-generator/django-admin-soft-dashboard.git
```

<br />

> Add `admin_soft` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_soft.apps.AdminSoftDashboardConfig',
        'django.contrib.admin',
    )
```

<br />

> 👉 Collect static if you are in production environment:

```bash
$ python manage.py collectstatic
```

<br />

> 👉 Start the app

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## Screenshots

![Django Admin Soft (Dark Mode) - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192209421-c71ebb42-7851-47eb-9942-6054e2010b82.jpg)

<br />

![Django Admin Soft (Login Page) - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192209441-2182d38f-814e-4123-ad54-7c3b580198fe.jpg) 

<br />

---
**Django Admin Soft Dashboard** - Open-source Django Admin THEME provided by **AppSeed [App Generator](https://appseed.us/)**
