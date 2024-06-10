# Generated by Django 5.0.2 on 2024-06-10 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_', '0001_initial'),
        ('client', '0002_job_type'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_details', models.CharField(max_length=500)),
                ('status', models.CharField(default='Unassigned', max_length=500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('employee_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_.location')),
            ],
        ),
    ]
