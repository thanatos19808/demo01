# Generated by Django 2.1.7 on 2019-03-27 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0054_auto_20190327_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
    ]
