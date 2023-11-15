# Generated by Django 4.2.6 on 2023-11-15 05:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shelters', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Withdrawn', 'Withdrawn')], max_length=10)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be between 10 and 15 digits.', regex='^\\d{10,15}$')])),
                ('email', models.EmailField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=7)),
                ('num_adults', models.IntegerField()),
                ('num_children', models.IntegerField()),
                ('residence', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse'), ('Mobile Home', 'Mobile Home')], max_length=50)),
                ('ownership', models.CharField(choices=[('Own', 'Own'), ('Rent', 'Rent')], max_length=50)),
                ('pet_alone_time', models.TextField(max_length=1000)),
                ('current_pets', models.TextField(max_length=1000)),
                ('daily_routine', models.TextField(max_length=1000)),
                ('expenses', models.TextField(max_length=1000)),
                ('previous_pets', models.TextField(max_length=1000)),
                ('reason', models.TextField(max_length=1000)),
                ('reference_name', models.CharField(max_length=50)),
                ('reference_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be between 10 and 15 digits.', regex='^\\d{10,15}$')])),
                ('reference_email', models.EmailField(max_length=254)),
                ('additional_comments', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default='default.jpg', upload_to='profile_photos/pets/')),
                ('name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Small Rodents', 'Small Rodents'), ('Reptiles', 'Reptiles'), ('Rabbits', 'Rabbits'), ('Horses', 'Horses'), ('Other', 'Other')], max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('medical_history', models.TextField(max_length=1000)),
                ('behavior', models.TextField(max_length=1000)),
                ('requirements', models.TextField(max_length=1000)),
                ('about', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Adopted', 'Adopted'), ('Pending', 'Pending'), ('Withdrawn', 'Withdrawn')], max_length=20)),
                ('application_deadline', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=2)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='shelters.petshelter')),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='pet_images/')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_images', to='pets.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_chats', to='pets.application')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_chats', to='accounts.petseeker')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_chats', to='shelters.petshelter')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='pets.pet'),
        ),
        migrations.AddField(
            model_name='application',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='accounts.petseeker'),
        ),
        migrations.AddField(
            model_name='application',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='shelters.petshelter'),
        ),
    ]
