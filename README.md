# Developer-road-website

The official website of developer road

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
python manage.py runserver
```

## Warning:

When registering a media photo is used in production.
Since the media files are served from cloudinary, some media files will be left like the default profile image, but don't worry.

The media files will serve correctly on production,or at least is what I think :).