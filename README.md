# Developer-road-website

The official website of developer road

Update: Heroku free plan is down, so there is no production link.
## Installation:

```python
pip install -r requirements.txt
```

From now you require a Postgres database with the following keys:

It shouldn't be like that but now it seems to break up if you don't set up a postgres database.

```python
'NAME': 'DeveloperRoad',
'USER': 'postgres',
'PASSWORD': 'daniel1404',
'HOST': 'localhost',
```

Now run:

```python
python manage.py livereload

python manage.py runserver
```

Remember to migrate the database before start developing:
```
python manage.py migrate
```


## Warning:

When registering a media photo is used in production.
Since the media files are served from cloudinary, some media files will be left like the default profile image, but don't worry.

The media files will serve correctly on production.


## Templates:
*Meta image*
Is the image that appears when the page is shared trough discord, telegram or whatsapp.

### Developing
Each template file **.html**, represents the template of a view, or a web component
