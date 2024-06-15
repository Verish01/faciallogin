# Generated by Django 5.0.6 on 2024-06-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('service_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
