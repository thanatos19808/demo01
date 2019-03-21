# Generated by Django 2.1.7 on 2019-03-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0016_auto_20190319_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consulta', models.DateField()),
                ('hora', models.CharField(max_length=5)),
                ('estatus', models.CharField(max_length=20)),
                ('consultorio', models.CharField(max_length=45)),
                ('motivo_consulta', models.CharField(max_length=200)),
                ('proxima_consulta', models.DateField()),
            ],
        ),
    ]