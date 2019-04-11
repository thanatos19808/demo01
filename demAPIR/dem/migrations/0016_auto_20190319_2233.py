# Generated by Django 2.1.7 on 2019-03-19 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0015_auto_20190319_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistente',
            name='Contraseña',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Contraseña'),
        ),
        migrations.AddField(
            model_name='asistente',
            name='Datos_personales',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Datos_personales'),
        ),
        migrations.AddField(
            model_name='asistente',
            name='Direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Direccion'),
        ),
        migrations.AddField(
            model_name='asistente',
            name='Telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Telefono'),
        ),
    ]
