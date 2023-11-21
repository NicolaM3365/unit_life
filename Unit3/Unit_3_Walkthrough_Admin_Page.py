"""
Unit 3 Walk through
Admin Page
Now we will learn how to access the admin page of the site.
We can use this to see the data on our site and use a friendly CRUD interface to manage it.

NOTE: Throughout this walkthrough we will be using the command line and changing the database
without changing anything about the code. For this reason, the code in this unit is identical
to that from partB of Unit 2.

#
#

1. Run your application with python manage.py runserver. Navigate to http://127.0.0.1:8000/admin

From here you will see the login page but at the moment it cannot be used as there are no default
credentials.

#
#

2. Create a "superuser" for us as the admin.

-> From the command line stop the development server with ctrl + c
-> In the command line type; python manage.py createsuperuser

    When you run this command you will get a string or errors.
    The last line as shown below points to the problem.

    django.db.utils.OperationalError: no such table: auth_user

    At the moment there is no database created for the project.

-> In the command line type; python manage.py makemigrations

    When you run the above you will see; No changes detected.

    We have not created any of our own database tables so this output is
    normal.

    makemigrations detects changes to the database and preps Django to update the changes.
    The updates are not applied at this point

-> In the command line type; python manage.py migrate

At this point the migrations will take effect.
In the command line you will see output similar to the following.

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK


At this point the error django.db.utils.OperationalError: no such table: auth_user
should be resolved when running python manage.py createsuperuser


-> In the command line type; python manage.py createsuperuser

Add in the details asked for example

    Username: stevek
    Email address: stephen.kohlmannucd@gmail.com
    Password:
    Password (again):
    This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]:
    Superuser created successfully.

Note that when entering a password in the command line you will not
see any input.

Note you can bypass a short password for the example.

#
#

3. Run your application with python manage.py runserver. Navigate to http://127.0.0.1:8000/admin

Login with your username and password and you will be able to see the Django administration page.

#
#

4. The admin page allows us to do a lot on the back-end. As a quick example navigate to the Users
folder and navigate to the current user you have created.

Note the encryption the Django has provided on your password. Django is not storing your plain text
password, but rather only a one-way encrypted version. So if it leaks out, it is not possible for a
hacker to get your password (although it could still help them to brute-force it, but that’s another story).

    Username:
    stevek
    Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    Password:
    algorithm: pbkdf2_sha256 iterations: 600000 salt: 5yas5L**************** hash: r8q0qq**************************************
    Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using this form.

#
#

5. Experiment with user management in the admin site.

Play some more with the User model in the admin site (127.0.0.1:8000/admin):
  Create a couple more more users
  Verify that a user without the Staff or Superuser fields checked cannot log into the admin site.
  Try changing user properties and resetting a password (note there's no way to see a passport)


********
This is it for now. If you haven't yet done so, now's a good time to learn more
about Django models by going through Part 2 of the official tutorial:
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
"""
