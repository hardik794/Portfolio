# Generated by Django 3.2 on 2021-05-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0004_auto_20210525_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='EndDate',
            field=models.DateField(),
        ),
    ]
