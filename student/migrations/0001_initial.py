# Generated by Django 3.2.9 on 2021-12-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.CharField(db_column='USN', max_length=50, primary_key=True, serialize=False)),
                ('semester', models.CharField(blank=True, db_column='Semester', max_length=10, null=True)),
                ('department', models.CharField(blank=True, db_column='Department', max_length=100, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]