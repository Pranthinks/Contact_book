# Generated by Django 4.2.4 on 2023-11-10 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name']},
        ),
    ]
