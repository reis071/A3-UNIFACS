# Generated by Django 5.0.6 on 2024-06-13 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0006_curso_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='professor',
        ),
    ]
