# Generated by Django 3.2.9 on 2021-11-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case_Proceeding_Details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('court_name', models.CharField(blank=True, max_length=200, null=True)),
                ('causelist_date', models.CharField(blank=True, max_length=200, null=True)),
                ('purpose', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DRT_Case_Status_Report_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('diary_no', models.CharField(blank=True, max_length=200, null=True)),
                ('case_type', models.CharField(blank=True, max_length=200, null=True)),
                ('case_no', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_filling', models.CharField(blank=True, max_length=200, null=True)),
                ('applicant', models.CharField(blank=True, max_length=200, null=True)),
                ('respondent', models.CharField(blank=True, max_length=200, null=True)),
                ('applicant_advocate', models.CharField(blank=True, max_length=200, null=True)),
                ('respondent_advocate', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drt_or_drat', models.CharField(blank=True, max_length=200, null=True)),
                ('party_name', models.CharField(blank=True, max_length=200, null=True)),
                ('no_of_applicants', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
