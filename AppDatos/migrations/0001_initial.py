# Generated by Django 4.1 on 2022-08-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_de_familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('anio_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
