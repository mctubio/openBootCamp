# Generated by Django 4.1.7 on 2023-02-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='cast',
            field=models.ManyToManyField(help_text='Actor/Actriz principales', to='catalog.cast'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(help_text='Genero de la pelicula', to='catalog.genre'),
        ),
        migrations.AlterField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(help_text='Idiomas', to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='film',
            name='sinopsis',
            field=models.TextField(help_text='Datos de la pelicula', max_length=1000),
        ),
    ]
