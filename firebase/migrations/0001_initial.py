# Generated by Django 3.1.2 on 2020-10-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('image', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
