# Life Project Django Application

## Overview

Life Project is a Django-based web application designed to provide a comprehensive platform for project management, blogging, messaging, and user management. This application leverages Django 4.2.7 and a suite of additional packages to create a feature-rich experience.

## Features

- **Project Management**: Organize and track projects efficiently.
- **Blogging**: A platform for users to write and publish blog posts.
- **Messaging**: A system for user-to-user communication.
- **User Management**: Registration, login, profile management, and password reset functionalities.

## Live Application

The application is deployed and can be accessed [here](https://life-project.onrender.com).

## Repository

Source code available on [GitHub](https://github.com/NicolaM3365/unit_life).

## Installation

To set up the Life Project application, follow these steps:

### Prerequisites

- Python 3.x
- PostgreSQL (or any other database system supported by Django)
- A virtual environment (recommended)


### Dependencies

Install the required dependencies by running:

```bash
pip install Django==4.2.7
pip install django-crispy-forms==2.1
pip install crispy-bootstrap5==2023.10
pip install Pillow==10.1.0
pip install Gunicorn==20.1.0
pip install whitenoise==5.3.0
pip install psycopg2==2.9.2
pip install dj-database-url==0.5.0


### Steps
# Clone the repository:
git clone https://github.com/NicolaM3365/unit_life.git


# Navigate to the root directory.

# Install the necessary packages.

# Run the application:

python manage.py


# Access 
- Open a web browser and visit http://localhost:8000/.


## Usage

# The main route '/' will either prompt you for login or show the home page if you're already logged in.
# Use the '/login' route to login. Logging in allows you to view the home page and read the Blog.
# The '/projectmanager' route shows the list of all projects including links to project tasks.
# The '/messaging' route shows all messages.
# Use the blog functionality by navigating to '/blog'.

## Security Notes
# If you have deployed your application without setting a strong, unique SECRET_KEY, it is crucial to update it immediately for production. Never use the default Django secret key in a production environment.
# Regularly rotate your secret keys as a security best practice.
# Always keep your secret keys confidential and out of version control systems.





