.. _config:

Configuration Commands and `config.py`
======================================

So lets go through each of the configuring variables.

APP_NAME is the name of the app. This is used in templating
to make sure that all the pages at least have the same html
title

SECRET_KEY is a alpha-numeric string that is used for crypto
related things in some parts of the application. Set it as an
environment variable or default to our insecure one. This is
used in password hashing see app/models/user.py for more info.
YOU SHOULD SET THIS AS A CONFIG VAR IN PRODUCTION!!!!

SQLALCHEMY_COMMIT_ON_TEARDOWN is used to auto-commit any sessions
that are open at the end of the 'app context' or basically the
current request on the application. But it is best practice
to go ahead and commit after any db.session is created

SSL_DISABLE is a boolean to used to enable adhoc ssl certificates (Self-signed) within the application.
The next version of the flask base would accomodate specificying certificates as files

MAIL... is used for sending emails using MailGun. This is further described in email.py.



