# Generated by Django 3.2.9 on 2021-11-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('property_type', models.CharField(blank=True, max_length=200, null=True)),
                ('detail_of_property', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
