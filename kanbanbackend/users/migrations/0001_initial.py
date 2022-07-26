# Generated by Django 3.2.14 on 2022-07-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('username', models.TextField(db_column='username')),
                ('password_hash', models.TextField(db_column='password_hash')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
