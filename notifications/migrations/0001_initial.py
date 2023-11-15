# Generated by Django 4.2.6 on 2023-11-15 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_object_id', models.PositiveIntegerField()),
                ('notification_type', models.CharField(choices=[('new_message', 'new_message'), ('application_status', 'application_status'), ('new_pet', 'new_pet'), ('review', 'review'), ('new_application', 'new_application')], max_length=50)),
                ('notification_object', models.PositiveIntegerField()),
                ('read', models.BooleanField(default=False)),
                ('sender_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_content_type', to='contenttypes.contenttype')),
            ],
        ),
    ]
