# Baiano Restaurant

## Table of Contents

- [Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
  - [Strategy (Site Goals)](#strategy-site-goals)
  - [Scope (User Stories)](#scope-user-stories)
  - [Structure (Design Choices)](#structure-design-choices)
  - [Skeleton (Wireframes)](#skeleton-wireframes)
  - [Surface (Visual Design)](#surface-visual-design)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Libraries & Frameworks](#libraries--frameworks)
  - [Tools](#tools)
- [Deployment](#deployment)
- [Existing Features](#existing-features)
- [Future Features](#future-features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Credits](#credits)

---

## Overview

The Baiano Restaurant is a fictional Brazilian restaurant, and the webpage was developed as a full-stack project for Code Institute Milestone 3. The webpage has a homepage introducing the restaurant, a menu page with its main dishes, and a login system that allows registered users to create, edit, and delete reservations.

Designed with a mobile-first approach, the website is fully responsive to ensure a consistent experience across all devices. It implements CRUD functionality, where registered users can manage their reservations, while the superuser can access the admin panel to oversee all bookings and make changes as needed.

[Back to the top](#table-of-contents)

## User Experience (UX)

Baiano Restaurant’s users are primarily people from Bahia, living abroad, and looking for Bahian food, often browsing on mobile while looking for a place to eat.

Customers want to quickly have a look at the menu with images, check opening hours, and book a table. Customers can manage existing reservations, while staff/admin users can review and update bookings. The experience should feel warm, vibrant, and reminiscent of home, and accessible for all users.

[Back to the top](#table-of-contents)

## Strategy (Site Goals)

The website aims to promote Baiano Restaurant by sharing authentic Bahian dishes, and creating a sense of home for people from Bahia living abroad.

It highlights the restaurant’s unique flavours and cultural background with pictures on the menu from the dishes made at the restaurant.

The webpage provides all essential information, such as menu, opening hours, and location, allowing customers to book tables online, by phone, or email.

A mobile-first design ensures that it looks and feels comfortable on all screen sizes.

For management, the admin area enables staff to review, edit, and organise reservations, helping the restaurant operate more efficiently.

[Back to the top](#table-of-contents)

## Scope (User Stories)

The project is organised and tracked on GitHub Projects, which can be viewed [here](https://github.com/users/faelf/projects/4).

The board displays all features categorised by their current status: To Do, In Progress, and Complete.

Each user story represents a feature or functionality for the website. They have been prioritised using the MoSCoW method (Must Have, Should Have, Could Have, Won’t Have), based on my current capabilities and future development goals. The project includes features I am currently able to develop, as well as others I plan to add in the future as I continue learning.

Below are the User Stories, with their acceptance criteria.

- [Restaurant Menu](https://github.com/faelf/baiano/issues/1)
- [Contact information and opening hours](https://github.com/faelf/baiano/issues/2)
- [Customer to make reservations online](https://github.com/faelf/baiano/issues/3)
- [Update menu items](https://github.com/faelf/baiano/issues/4)
- [Navigation to all pages](https://github.com/faelf/baiano/issues/5)
- [Contact form](https://github.com/faelf/baiano/issues/6)
- [Restaurant map location](https://github.com/faelf/baiano/issues/7)
- [Customer reviews](https://github.com/faelf/baiano/issues/8)
- [Social media links](https://github.com/faelf/baiano/issues/9)
- [Admin reviews management](https://github.com/faelf/baiano/issues/10)

[Back to the top](#table-of-contents)

## Structure (Design Choices)

### Templates

A `base.html` template defines what is seen on every page, including the navigation bar and footer, with content injected via {% block content %}, so when the customer clicks on the `Menu` page, the `menu.html` page will extend the `base.html`. Ensuring consistancy across all pages.

### Static Files

Static files such as CSS, JavaScript, and images, are managed using Django’s {% static %} tag.

### Responsive Design

Bootstrap was chosen for its ease of creating a responsive design, and minimising the need for custom CSS media queries. Its column design makes it a simple way for the content on the page to adjust for various screen sizes, speeding up development and improving maintainability.

Images are set with `max-width` to ensure that they stay responsive, and they will not over grow and feel disproportional.

[Back to the top](#table-of-contents)

## Skeleton (Wireframes)

[Back to the top](#table-of-contents)

## Surface (Visual Design)

### Colour Palette

The colour palette is inspired by the vibrant culture of Bahia.

- **Primary Blue:**
- **Secondary Yellow:**
- **Green:**
- **Red:**
- **Light Tones:**

### Typography

- **Fonts:**
  - **Headings:**
  - **Body Text:**

[Back to the top](#table-of-contents)

## Technologies Used

### Languages

### Libraries & Frameworks

- [Django](https://docs.djangoproject.com/en/5.2/topics/install/)
- [gunicorn](https://gunicorn.org/)
- [psycopg](https://pypi.org/project/psycopg2/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html)

### Tools

[Back to the top](#table-of-contents)

## Deployment

A step-by-step guide to deploying your Django project to Heroku on Windows.

### GitHub Setup

1. Create a new repository on GitHub.
2. Clone the repository to your local machine.

### VS Code Setup

1. Open the cloned repository in VS Code.
2. Create a virtual environment.
3. Install Django. `pip install django`
4. Create the project. `django-admin startproject (Project name) .`
5. Create an app. `python manage.py startapp (App name)`
6. Create a simple HttpResponse view for the homepage.
7. Install Gunicorn. `pip install gunicorn`
8. Create a `Procfile` with the command: `web: gunicorn (Project name).wsgi `
9. In settings.py add:

```python
WSGI_APPLICATION = '(Project name).wsgi.application'
```

10. Specify the Python version for your development environment using a `.python-version` file.
11. Add `heroku` and `localhost` to the `ALLOWED_HOSTS` in `settings.py`.

```python
ALLOWED_HOSTS = [
    '.herokuapp.com',
    'localhost',
    '127.0.0.1',
]
```

12. Create a database.
13. Create an `env.py` file and add the `DATABASE_URL` and `SECRET_KEY`.

```python
import os

os.environ.setdefault(
    "DATABASE_URL", "(Database URL)")

os.environ.setdefault("SECRET_KEY", "(Create a key)")
```

14. Install `psycopg2`. `pip install psycopg2`
15. Install `dj-database-url`. `pip install dj-database-url`
16. Add to `settings.py`.

```python
import os

import dj_database_url
if os.path.isfile('env.py'):
    import env

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

17. Run your first migration `python manage.py migrate`.
18. Create a superuser. `python manage.py createsuperuser`
19. Install `whitenoise` for static files. `pip install whitenoise`
20. Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE list`, above all other middleware apart from `Django’s SecurityMiddleware`:

```python
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

21. Add the following to the bottom of your `settings.py` file:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

22. Run `collectstatic` to gather static files for production. `python manage.py collectstatic`
23. Create requirements file. `pip freeze > requirements.txt`
24. Commit all changes and push to GitHub.

### Heroku Deployment

1. Log in to the Heroku dashboard.
2. Click **New** and select **Create new app**.
3. Enter a unique app name.
4. Choose the deployment region.
5. In **Settings**, add all necessary config vars including:
   - Database URL
   - Secret key
6. Under **Deployment method**, connect the app to your GitHub repository.
7. Press **Deploy**
8. Test the deployed site thoroughly to ensure all features work as expected.

[Back to the top](#table-of-contents)

## Existing Features

### Navigation

- A responsive navigation bar is present on all pages, providing consistent access to all pages.
- **Dynamic Links:** The navigation bar dynamically adapts based on user authentication.
  - **Authenticated Users:** See links for `My Bookings` and `Log out`.
  - **Unauthenticated Users:** See links for `Log in` and a `Register` button.

### Homepage

The homepage introduces the restaurant, and at the same time being functional.

- **Hero Section:** A full-width hero image with a welcoming message and large buttons for the customer to easily book a table or register in the restaurant.
- **Popular Choices:** This section displays featured dishes with images and brief descriptions, giving users a quick taste of the menu.
- **Customer Reviews:** To create a connection between customers and the restaurant.
- **About Us:** This final section tells the story of the restaurant.

### Footer

- **Social Media:**
- **Contact Information:**
- **Location:**
- **Opening Hours:**

### Login & Registration

These features provide the main functionality, and enable a personalised experience for each user by allowing them to manage their bookings and access user-specific content.

### Reservations

The `My Bookings` page is designed as a user page, where customers can view and manage their reservations, and feel it is their space on the webpage, implementing full CRUD functionality for managing reservations.

- **Read:** Users can view all their reservations in a card layout ordered by date.
- **Create:** The `New Booking` button allows users to easily make a new reservation.
- **Update:** Clicking `Edit` enables the `Save` and `Cancel` buttons, providing an intuitive editing experience.
- **Delete:** The `Delete` button redirects the customer to a confirmation page, where they can delete or keep their reservation.

[Back to the top](#table-of-contents)

## Future Features

[Back to the top](#table-of-contents)

## Testing

[Back to the top](#table-of-contents)

## Bugs

[Back to the top](#table-of-contents)

## Credits

### Code

### Reference Pages

### Media

- Menu
  - The images were taken from the pages below
  - Bobó de Camarão - https://www.sumerbol.com.br/uploads/images/2021/06/bobo-de-camarao-1134-1624568462.jpg
  - Moqueca Baiana - https://foodandroad.com/wp-content/uploads/2021/06/img-brazil-moqueca-15-500x500.jpg
  - Acarajé - https://assets.tastemadecdn.net/images/286b17/1231874d2fa30f09baa7/cce93d.jpg
  - Abará - https://instadelivery-public.nyc3.cdn.digitaloceanspaces.com/itens/1701525573656b38459c900_75_75.jpeg
  - Caruru - https://canaldareceita.com.br/wp-content/uploads/2025/03/CARURU-720x720.jpg
  - Xinxim de Galinha - https://nacolher.com/wp-content/uploads/2022/10/como-fazer-xinxim-de-galinha.jpg
  - Feijoada - https://th-thumbnailer.cdn-si-edu.com/6yQXolz5w833JwZEsjOWR2TJjiY=/1280x1280/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/a2/af/a2af930e-aa90-412b-9ec8-b0de651d5fa7/feijoada-brazil-world-cup.jpg
  - Pão de Queijo - https://static01.nyt.com/images/2024/12/19/multimedia/KF-Pao-de-Queijorex/KF-Pao-de-Queijorex-mediumSquareAt3X-v2.jpg
  - Coxinha - https://www.beths.uk/cdn/shop/products/coxinha03_40cab723-f1ab-4310-9222-5356ae659e47_1445x.png?v=1719501444
  - Pastel - https://thumbs.dreamstime.com/b/pastel-brasile%C3%B1o-de-la-comida-homemade-121303554.jpg
  - Brigadeiro - https://bonnibakery.com/wp-content/uploads/2024/08/Brigadeiro_206-1.jpg
  - Quindim - https://divaliciousrecipes.com/wp-content/uploads/2014/02/quindim.jpg

[Back to the top](#table-of-contents)
