# Generated by Django 4.1.7 on 2023-03-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_usercartmodel_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
