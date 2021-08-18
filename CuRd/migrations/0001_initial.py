# Generated by Django 3.2.5 on 2021-08-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=100)),
                ('Roll_Number', models.PositiveIntegerField()),
                ('Year_Of_Joining', models.PositiveIntegerField()),
                ('Course', models.CharField(choices=[('CSE', 'CSE'), ('ME', 'ME'), ('CIVIL', 'CIVIL'), ('EE', 'EE')], max_length=100)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
