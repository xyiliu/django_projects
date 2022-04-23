# Generated by Django 3.2.5 on 2022-02-25 17:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Breed must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horses.breed')),
            ],
        ),
    ]
