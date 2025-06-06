# Generated by Django 5.2.1 on 2025-05-28 00:53

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plataforma', '0002_remove_curso_alumnos_curso_alumno_cursos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido_html', ckeditor.fields.RichTextField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiales', to='Plataforma.curso')),
            ],
        ),
    ]
