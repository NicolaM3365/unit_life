# Unit 1 Walk through
# Django Installation

# Read the instructions for each of the following activities, and run them one by one in the terminal.

# *** Activity 0a - Create a virtual environment (optional) ***
python -m venv your_env_name

# *** Activity 0b - Activate the virtual environment ***
# -->If on Git bash/macOS/Linux:
    source your_env_name/bin/activate
# --> If on Windows Command Prompt (cmd):
    your_env_name/Scripts/activate.bat


# *** Activity 1 - Install Django inside the virtual environment ***
pip install django


# *** Activity 2 - Confirm successful installation (you should have version 4.2 or higher):
python -m django --version


# *** Activity 3 - Check the Django-admin tool ***
django-admin
# The above will show available sub commands. For now we will use only startproject.

# *** Activity 4 - Create a new project ***
django-admin startproject django_project
# The command above will create a Django project directory. The directory name will be
# django_project. The name should be relevant to your project.

# *** Activity 5 - Familiarise yourself with the "skeleton" project tree
# Look at the directory structure either in Terminal/VS Code/Sublime etc. Glance at each of the files.

# (If on Mac, a handy tool to view the tree structure can be installed with brew install tree.
# More details here https://michaelsoolee.com/tree-tool/)

# ├── django_project
# │   ├── __init__.py
# │   ├── asgi.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# └── manage.py



# *** Activity 6 - Inspect manage.py ***
# manage.py is at the base level and allows us to run command line commands.
# We are not changing this file. Open file to see the contents.


# *** Activity 7 - Look at the django-project directory ***
# This directory includes the general files for the entire project.


# *** Activity 8 - init.py ***
#  This empty file just tells Python that this is a python package.


# *** Activity 9 - settings.py ***
# This is the main configuration file we will use as we build our project. For now note:
# SECRET_KEY
# DEBUG = TRUE
# DATABASES
# APPS


# *** Activity 10 - urls.py ***
# This is where we set up our urls routes - mapping between url patterns and the associated view function.
# At the moment we have the default admin route.

    # urlpatterns = [
    #     path("admin/", admin.site.urls),
    # ]

# We will see how this works when we add more routes


# *** Activity 11 -wsgi.py and asgi.py ***
# These files definehow are python project and the web server (e.g. gunicorn) communicate.
# Django sets up a default configuration of these files.

# WSGI is the main Python standard for communicating between web servers and applications, but it only supports synchronous code.
# ASGI is the newer, asynchronous-friendly standard that allows Django to use asynchronous Python features (mostly out of scope).


# *** Activity 12 - Run the server ***
python manage.py runserver
# The above command will run the basic server. You should see something like the following:

#     Watching for file changes with StatReloader
#     Performing system checks...

#     System check identified no issues (0 silenced).

#     You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
#     Run 'python manage.py migrate' to apply them.

#     July 11, 2023 - 12:44:54
#     Django version 4.2.3, using settings 'django_project.settings'
#     Starting development server at http://127.0.0.1:8000/
#     Run 'python manage.py migrate' to apply them.
#     Quit the server with CONTROL-C.

# Note the warnings and the suggestion.
# Run 'python manage.py migrate' to apply the default migrations.

# We will come back to this again

# *** Activity 12 - Access the default site in the browser ***
# Navigate in the browser to http://127.0.0.1:8000/ or localhost:8000
# You shouldn't see any content there just yet

# *** Activity 13. Access the admin site ***
# Navigate to the admin page: http://localhost:8000/admin/
# It will ask for a user and password, we will continue with this next time.

# *** Activity 14 - Stop the server ***
# Stop the server using ctrl + c (to start it again, use: python manage.py runserver)
