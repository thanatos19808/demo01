# Generated by Django 2.1.7 on 2019-03-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0060_auto_20190328_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='estado_nacimiento',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='monoclave',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='municipio_nacimiento',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
