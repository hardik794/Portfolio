# Generated by Django 3.2 on 2021-10-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('BirthDate', models.DateField()),
                ('Github', models.URLField()),
                ('Linkdein', models.URLField()),
                ('Youtube', models.URLField()),
                ('logo', models.ImageField(upload_to='pic')),
                ('Profilepic', models.ImageField(upload_to='pic')),
                ('Bannerpic', models.ImageField(upload_to='pic')),
                ('Aboutpic', models.ImageField(upload_to='pic')),
                ('CurrentStatus', models.CharField(max_length=100)),
                ('Proffesion1', models.CharField(default='developer', max_length=100)),
                ('Proffesion2', models.CharField(default='developer', max_length=100)),
                ('Proffesion3', models.CharField(default='developer', max_length=100)),
                ('Proffesion4', models.CharField(default='developer', max_length=100)),
                ('AboutTitle', models.CharField(default='Title', max_length=100)),
                ('AboutPicTitle', models.CharField(default='TitlePic', max_length=100)),
                ('AboutPicDesc', models.TextField(default='Title Decription')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Year', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('CenterName', models.CharField(max_length=100)),
                ('Discription', models.TextField(default='Discription')),
                ('RankType', models.CharField(max_length=100)),
                ('Status', models.BooleanField()),
                ('Rank', models.CharField(max_length=100)),
                ('Colour', models.CharField(default='black', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=100)),
                ('joinDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Status', models.BooleanField(default=False)),
                ('Organization', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Colour', models.CharField(default='black', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtherDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skillquote1', models.CharField(max_length=100)),
                ('Skillquote2', models.CharField(max_length=100)),
                ('Softquote1', models.CharField(max_length=100)),
                ('Softquote2', models.CharField(max_length=100)),
                ('Tagquote1', models.CharField(max_length=100)),
                ('Tagquote2', models.CharField(max_length=100)),
                ('Tagquote3', models.CharField(max_length=100)),
                ('Featurepic', models.FileField(upload_to='pic')),
                ('Tagpic', models.FileField(upload_to='pic')),
                ('Bannerbackground', models.FileField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=100)),
                ('Technology', models.CharField(default='null', max_length=200)),
                ('Discription', models.TextField(default='null')),
                ('ProjectLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MyResume', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SkillName', models.CharField(max_length=100)),
                ('Rank', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SoftwareName', models.CharField(max_length=100)),
                ('Softwareimage', models.ImageField(upload_to='pic')),
            ],
        ),
    ]