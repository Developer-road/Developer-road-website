# Generated by Django 3.1.4 on 2021-03-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
