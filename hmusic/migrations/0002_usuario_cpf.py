# Generated by Django 4.2.5 on 2023-10-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmusic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
    ]
