# Generated by Django 3.1.4 on 2021-01-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20210118_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
