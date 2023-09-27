# Generated by Django 4.2.5 on 2023-09-27 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_instrumentos')),
                ('descricao', models.TextField(max_length=1000)),
                ('categoria', models.CharField(choices=[('BATERIA', 'Bateria'), ('CORDAS', 'Cordas'), ('ELETRONICO', 'Eletronico'), ('METAIS', 'Metais'), ('PERCUSAO', 'Percusao'), ('SOPRO', 'Sopro'), ('TECLAS', 'Teclas'), ('ACESSORIOS', 'Acessorios')], max_length=15)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]