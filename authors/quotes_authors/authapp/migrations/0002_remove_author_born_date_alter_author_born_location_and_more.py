# Generated by Django 4.2.4 on 2023-09-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='born_date',
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]