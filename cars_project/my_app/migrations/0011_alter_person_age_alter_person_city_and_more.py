# Generated by Django 4.2.2 on 2023-06-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]