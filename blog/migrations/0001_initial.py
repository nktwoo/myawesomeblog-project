# Generated by Django 3.2.5 on 2021-07-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
