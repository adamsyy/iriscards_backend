# Generated by Django 3.2 on 2023-02-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20230206_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
