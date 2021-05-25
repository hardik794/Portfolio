# Generated by Django 3.2 on 2021-05-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0003_basicdetails_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='Technology1',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='Technology2',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='Technology3',
        ),
        migrations.AddField(
            model_name='projects',
            name='Discription',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='projects',
            name='Technology',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='Description',
            field=models.TextField(),
        ),
    ]