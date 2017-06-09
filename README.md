[![Stories in Ready](https://badge.waffle.io/infrascloudy/flask-base.png?label=ready&title=Ready)](https://waffle.io/infrascloudy/flask-base?utm_source=badge)
# Flask-Base

A Flask application template with the boilerplate code already done for you.

**Documentation available at [http://flask-base.readthedocs.io/](http://flask-base.readthedocs.io/).**

## What's included?

* Blueprints
* User and permissions management
* Flask-SQLAlchemy for databases
* Flask-WTF for forms
* Flask-Assets for asset management and SCSS compilation
* Flask-Mail for sending emails
* gzip compression
* Redis Queue for handling asynchronous tasks
* ZXCVBN password strength checker  
* CKEditor for editing pages

## Setting up

##### Clone the repo

```
$ git clone https://github.com/infrascloudy/flask-base.git
cd flask-base
```

##### Initialize a virtualenv

```
$ pip install virtualenv
$ virtualenv -p /path/to/python3.x/installation env
$ source env/bin/activate
```

For mac users it will most likely be
```
$ pip install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```
Note: if you are using a python2.x version, point the -p value towards your python2.x path

##### (If you're on a mac) Make sure xcode tools are installed

```
$ xcode-select --install
```

##### Add Environment Variables 

Create a file called `config.env` that contains environment variables in the following syntax: `ENVIRONMENT_VARIABLE=value`. For example,
the mailing environment variables can be set as the following. We recommend using MailGun for a mailing SMTP server. 

```
MAIL_NAME = 'My Visible Name'
MAIL_ADDRESS = 'no-reply@mydomain.com'
MAIL_DOMAIN = 'mg.example.com'
MAIL_API = 'key-deadb33fdeadb33fdeadb33f'
SECRET_KEY=SuperRandomStringToBeUsedForEncryption
```

Other Key value pairs:

* `ADMIN_EMAIL`: set to the default email for your first admin account (default is `admin@example.com`)
* `ADMIN_PASSWORD`: set to the default password for your first admin account (default is `password`)
* `DATABASE_URL`: set to a postgresql database url (default is `data-dev.sqlite`)
* `REDISTOGO_URL`: set to Redis To Go URL or any redis server url (default is `http://localhost:6379`)
* `RAYGUN_APIKEY`: api key for raygun (default is `None`)
* `FLASK_CONFIG`: can be `development`, `production`, `default`, `heroku`, `unix`, or `testing`. Most of the time you will use `development` or `production`. 

**Note: do not include the `config.env` file in any commits. This should remain private.**

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Other dependencies for running locally

You need [Redis](http://redis.io/), and [Sass](http://sass-lang.com/). Chances are, these commands will work:


**Sass:**

```
$ gem install sass
```

**Foreman:**

```
$ gem install foreman
```
**Redis:**

_Mac (using [homebrew](http://brew.sh/)):_

```
$ brew install redis
```

_Linux:_

You may need to install libpq-dev

```
$ sudo apt-get install redis-server libpq-dev
```

You will also need to install **PostgresQL**

_Mac (using homebrew):_

```
brew install postgresql
```

##### Create the database

```
$ python manage.py recreate_db
```

##### Other setup (e.g. creating roles in database)

```
$ python manage.py setup_dev
```

Note that this will create an admin user with email and password specified by the `ADMIN_EMAIL` and `ADMIN_PASSWORD` config variables. If not specified, they 
are both `admin@example.com` and `password` respectively.

##### [Optional] Add fake data to the database

```
$ python manage.py add_fake_data
```

## Running the app

```
$ source env/bin/activate
$ foreman start -f Local
```

## Formatting code

Before you submit changes to flask-base, you may want to autoformat your code with 
`python manage.py format`.

## Contributing

Contributions are welcome! Check out our [Waffle board](https://waffle.io/infrascloudy/flask-base) which automatically syncs with this project's GitHub issues.

## Documentation Changes

Documentation gets built by ReadTheDocs.
The files are all located here, under docs/source

## License
[MIT License](LICENSE.md)
