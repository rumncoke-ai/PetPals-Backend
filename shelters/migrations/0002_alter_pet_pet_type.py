# Generated by Django 4.2.6 on 2023-11-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Small Rodents', 'Small Rodents'), ('Reptiles', 'Reptiles'), ('Rabbits', 'Rabbits'), ('Horses', 'Horses'), ('Other', 'Other')], max_length=100),
        ),
    ]