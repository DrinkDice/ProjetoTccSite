# Generated by Django 4.2.5 on 2023-10-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmusic', '0003_instrumentos_numero_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
