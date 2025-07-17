# Baiano Restaurant

## Deployment

Here is a step by step how I deployed in Heroku

### GitHub

1. Create a new repository in GitHub
2. Clone the repository
3. Install Django, and create the project
4. Create a simple view for the home page
5. Install gunicorn
6. Add Heroku and Localhost to Allowed Hosts
7. Craete the database
8. Create env.py file, and add the database url
9. Install psycopg2 and dj-database-url
10. After connecting to the database, migrate the models

### Heroku

1. Login to Heroku
2. Click on 'New'
3. From the 'New' dropdown, click on 'Create new app'
4. Give it a name
5. Choose a location
6. In your app, go to settings, and add the database url
7. On deployment method, link to the GitHub repository

