# Generated by Django 3.2.2 on 2021-05-06 10:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('poster', models.CharField(max_length=200)),
            ],
        ),
    ]
