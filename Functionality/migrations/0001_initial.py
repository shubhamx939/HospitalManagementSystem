# Generated by Django 3.2.16 on 2022-12-29 13:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor_id', models.CharField(blank=True, max_length=100, null=True)),
                ('accountant_id', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.CharField(blank=True, max_length=100, null=True)),
                ('end_date', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodbank_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('donor', models.BooleanField(default=False)),
                ('withdrawer', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('patient', models.BooleanField(default=False)),
                ('individual', models.BooleanField(default=False)),
                ('datetime', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
