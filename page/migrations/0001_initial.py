# Generated by Django 2.0.7 on 2018-08-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=140)),
                ('Description', models.TextField(max_length=140)),
                ('Photo', models.FileField(upload_to='')),
            ],
        ),
    ]
