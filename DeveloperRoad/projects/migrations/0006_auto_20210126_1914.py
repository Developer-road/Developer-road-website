# Generated by Django 3.1.4 on 2021-01-26 19:14

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210104_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=projects.models.get_project_image),
        ),
    ]