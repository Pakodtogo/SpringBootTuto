# Generated by Django 5.0.1 on 2024-01-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashpower', '0002_alter_abonne_adresse_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tranchetarif',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]