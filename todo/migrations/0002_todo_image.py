# Generated by Django 3.0.6 on 2020-08-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(default='baby_5', upload_to='images/'),
            preserve_default=False,
        ),
    ]
