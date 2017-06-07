.. _commands:

Manage.py and Commands
======================

`python manage.py runserver`
----------------------------

A note about python manage.py runserver.
Runserver is actually located in flask_script.
Since we have not specified a runserver command, it defaults to
flask_script's Server() method which calls the native
flask method app.run().
You can pass in some arguemnts such
as changing the port on which the server is run.

`.env`
------

The following code block will look for a '.env' file which
contains environment variables for things like email address
and any other env vars. The .env file will be parsed and
santized.
Each line contains some "NAME=VALUE" pair.
Split this and then store var[0] = "NAME" and var[1] = "VALUE".
Then formally set the environment variable in the last line of
this block.
Per our running example, os.environ["NAME"] = "VALUE"
These environment variables can be accessed with "os.getenv('KEY')"

::python

    if os.path.exists('.env'):
        print('Importing environment from .env file')
        for line in open('.env'):
            var = line.strip().split('=')
            if len(var) == 2:
                os.environ[var[0]] = var[1]

Config and `create_app`
-----------------------

