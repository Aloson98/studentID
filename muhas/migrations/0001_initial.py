# Generated by Django 4.2.6 on 2023-10-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('registration_number', models.IntegerField()),
                ('expire_date', models.DateTimeField()),
                ('student_pic', models.ImageField(upload_to='passport')),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
