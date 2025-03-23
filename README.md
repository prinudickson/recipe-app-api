# recipe-app-api
Recipe API Project

# Run Flake8 
`pdickson004@NL_YRY2K5F7L7 recipe-app-api % docker-compose run --rm app sh -c "flake8"`

# Install/ Create Django Project
`pdickson004@NL_YRY2K5F7L7 recipe-app-api % docker-compose run --rm app sh -c "django-admin startproject app ."`

# Run Tests
`(recipe-app-api) pdickson004@NL_YRY2K5F7L7 recipe-app-api % docker-compose run --rm app sh -c "python manage.py test"`

# Working with DB in Docker [NEVER RAN THIS!]
`docker exec -it my_postgres psql -U postgres -d mydb`

# Creating a new app in Django
`(recipe-app-api) pdickson004@NL_YRY2K5F7L7 recipe-app-api % docker-compose run --rm app sh -c "python manage.py startapp core"`