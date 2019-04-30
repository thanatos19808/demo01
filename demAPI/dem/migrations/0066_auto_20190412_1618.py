# Generated by Django 2.1.7 on 2019-04-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0065_auto_20190328_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistente',
            name='Contraseña',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Contraseña',
        ),
        migrations.AddField(
            model_name='asistente',
            name='estatus',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='estatus',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='nombre_sub_especialidad',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estatus',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='permisos',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='cedula',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
