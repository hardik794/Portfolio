# Generated by Django 3.2 on 2021-06-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0005_auto_20210525_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='Backgroundimage',
            field=models.ImageField(upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='MyMainimage',
            field=models.ImageField(upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='Myimage',
            field=models.ImageField(upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='logo',
            field=models.ImageField(upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='MyResume',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='Softwareimage',
            field=models.ImageField(upload_to='pic'),
        ),
    ]
