# Generated by Django 5.1 on 2024-08-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_ownership_ended_alter_ownership_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время бронирования'),
        ),
    ]
