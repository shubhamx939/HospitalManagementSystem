# Generated by Django 3.2.16 on 2022-12-29 10:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0006_auto_20221227_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountant_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('accountant_name', models.CharField(blank=True, max_length=50, null=True)),
                ('accountant_email', models.CharField(blank=True, max_length=50, null=True)),
                ('accountant_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('accountant_address', models.CharField(blank=True, max_length=150, null=True)),
                ('accountant_gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Labouratorist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labouratorist_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('labouratorist_name', models.CharField(blank=True, max_length=50, null=True)),
                ('labouratorist_email', models.CharField(blank=True, max_length=50, null=True)),
                ('labouratorist_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('labouratorist_address', models.CharField(blank=True, max_length=150, null=True)),
                ('labouratorist_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('labouratorist_license', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('nurse_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nurse_email', models.CharField(blank=True, max_length=50, null=True)),
                ('nurse_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('nurse_address', models.CharField(blank=True, max_length=150, null=True)),
                ('nurse_gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_age', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_email', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('patient_address', models.CharField(blank=True, max_length=150, null=True)),
                ('patient_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_blood', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_height', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_weight', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacist_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True)),
                ('pharmacist_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pharmacist_email', models.CharField(blank=True, max_length=50, null=True)),
                ('pharmacist_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('pharmacist_address', models.CharField(blank=True, max_length=150, null=True)),
                ('pharmacist_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('pharmacist_license', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialty',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_license',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_speciality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
