# Generated by Django 4.1.3 on 2022-11-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_associacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Nome'),
        ),
    ]
