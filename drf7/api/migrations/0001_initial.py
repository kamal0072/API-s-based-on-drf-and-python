# Generated by Django 3.1.6 on 2021-03-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=120)),
                ('c_address', models.CharField(max_length=130)),
                ('c_moblile', models.IntegerField()),
                ('c_dob', models.DateField()),
            ],
        ),
    ]
