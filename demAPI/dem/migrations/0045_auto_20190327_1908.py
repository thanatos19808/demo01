# Generated by Django 2.1.7 on 2019-03-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0044_auto_20190325_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='nombre_doctor',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='rfc_doctor',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
