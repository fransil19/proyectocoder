# Generated by Django 3.2.9 on 2022-03-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id',
        ),
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
