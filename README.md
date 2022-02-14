# Flask base code

Use this codebase to start a wsgi flask project

## Stack

- flask as the main application engine
- flask-jwt as the db manager
- flask-bcrypt as the password hasher
- gunicorn as a launcher

## Requirements

- Python 3.6 or later
- python3-venv
- MongoDB 4.2 or later

## Install

```bash
git clone https://gitlab.com/gl-prout/socle-flask.git
cd socle-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp app/app-config.cfg.dist app/app/app-config.cfg
cp application.wsgi.dist application.wsgi
```

The scripts `config.sh` (if not contributing to the codebase) and `config-dev.sh` (if contributing to the codebase) can be used after cloning the repository.

```bash
sh config.sh
```
or
```bash
sh config-dev.sh
```

The `requirements.txt` was generated using `pipreqs` instead of `pip freeze`

Consider using `pipreqs . --force` instead of `pip freeze` so the file won't be bloated with unrequited python modules or broken dependency version. After the `requirements.txt` has been overwritten, append the line `gunicorn==20.0.4` at the end of the file if you wish to continue launching the application using `gunicorn`.

## Launch

```bash
gunicorn -b 0.0.0.0:5000 app.webapp:app --reload
```

It will launch the application inside a `gunicorn` container.

Available routes are:

- `GET - /` as the home route
- `POST - /user/subscribe` as the signup route
- `POST - /login` as the login route
- `GET - /user/profile` requiring a `Bearer token` obtained from `/login` to retrieve current user information
- `POST - /posts/create` for creating a post
- `PUT - /posts/update` for updating a post
- `GET - /posts/mine` for getting current user posts
- `GET - /posts/{post_id}` for getting a specific post
- `DELETE - /posts/{post_id}` for deleting a specific post created by the current user

## Api documentation

To access the api definition, the route is:

```text
[GET] /apidoc/api.yml
```

And to access the Swagger documentation, the route is:

```text
[GET] /api/docs
```

It may still get a little buggy, but you may be able to understand how it works.

## Docker

Do not use the dockers yet, composing for mongodb is still a WIP

## Configuration

The main configuration file is `app/app-config.cfg` where you can configure:

- mongodb settings
- secret key used by bcrypt and jwt to hash and compare passwords on login
- the login route
- the username login property
- the token header
- the base url for your application
- the absolute path from where the application is running
- the absolute path where the application sits
- the absolute path where you will upload files
- the relative path where you will upload files
- the max size of files to be uploaded

## Architecture

Your main source code sits in the `app` folder.

### controller

This layer is where you will define the routes of your application

### services

This layer is where most of your logic will be coded, called mainly from the controller layer

### repository

This layer is where you will code data related common manipulations, called mainly from the services layer

### data

This layer is where you will mostly code your data models, called mainly by the repository layer

### common

This layer is used for common functions which can be used anywhere in the other layers, called mainly by the services and repository layers

### static

If you use templates, the `static` folder can be used to place assets like favicons or stylesheets

### templates

If you use templates, here is where your Jinja2 templates will sit

## Special files

- `__init__.py` is where you set up external python or flask modules
- `constants.py` is where you can define constants to be used anywhere in the app
- `webapp.py` is the main entrypoint to your application

## Serving using WSGI

You will have to install the requirements system-wide instead of inside a python virtualenv.

You will also have to configure your virtualhost like this

```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName www.example.com

    WSGIDaemonProcess www.example.com user=www-data group=www-data threads=5 processes=2
    WSGIProcessGroup www.example.com
    WSGIScriptAlias / /var/www/www.example.com/application.wsgi
    WSGIPassAuthorization on

    ErrorLog /var/www/www.example.com/logs/error.log
    CustomLog /var/www/www.example.com/logs/access.log combined

    Alias /static/ /var/www/www.example.com/app/static/
    Alias /uploads/ /var/www/www.example.com/app/uploads/
    Alias /templates/ /var/www/www.example.com/app/templates/

    <Directory /var/www/www.example.com>
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>

</VirtualHost>
```

Note that if you serve using WSGI, you have to symlink your `templates` folder into the project root folder.

## Response

To compose a `JSON` response, use the `app/common/response.py` `response(success=True, message='Success', data={})` function to structure your response uniformly.

### Success

```json
{
    "success": true,
    "message": "Message",
    "data": {
        "properties": "values"
    }
}
```

### Error

```json
{
    "success": false,
    "message": "Message",
    "data": {
        "properties": "values"
    }
}
```

To render a template, use the flask default `render_template` function.
