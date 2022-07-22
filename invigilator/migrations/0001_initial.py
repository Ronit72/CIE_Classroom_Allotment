# Generated by Django 3.2.9 on 2021-12-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invigilator',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('invigilation_count', models.IntegerField(blank=True, db_column='Invigilation_count', null=True)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'invigilator',
                'managed': False,
            },
        ),
    ]
