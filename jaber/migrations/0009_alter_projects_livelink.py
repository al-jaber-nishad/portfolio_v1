# Generated by Django 3.2.9 on 2021-11-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaber', '0008_alter_projects_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='liveLink',
            field=models.URLField(blank=True),
        ),
    ]