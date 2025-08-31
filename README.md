# Developer-road-website

The open source code for the DeveloperRoad project. Made with Django 5.2, supporting PostgreSQL and media files via Cloudinary.

![DeveloperRoad site](/static/images/Readme/Developer-road-home-page.png)

## Run in Local:


Clone the repository.

```bash
git@github.com:Developer-road/Developer-road-website.git
cd Developer-road-website
```

Use a virtual environment to install the dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

By default DEBUG is False. This allows to run locally with an Sqlite local database.

To create the database locally, run:
```
python manage.py migrate
```

To run the project locally, use livereload if you're modifying the source code.

```python
python manage.py livereload

```

And in a separate terminal:

```
python manage.py runserver
```

## Warning:

When creating an user a media photo is used in production.
Since the media files are served from cloudinary, some media files will be left like the default profile image, but don't worry.

The media files will serve correctly on production.


## Templates:
*Meta image*
Is the image that appears when the page is shared trough discord, telegram or whatsapp.

### Developing
Each template file **.html**, represents the template of a view, or a web component
