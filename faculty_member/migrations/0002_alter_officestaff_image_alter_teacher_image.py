# Generated by Django 5.0.1 on 2024-06-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officestaff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
