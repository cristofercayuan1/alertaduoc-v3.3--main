# Generated by Django 5.0.6 on 2024-05-08 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_Qr',
            fields=[
                ('idQr', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('imagenqr', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDep', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombredep', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('apoyo', 'Personal de Apoyo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('idEspacio', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombreEspacio', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('codigo_qr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud.codigo_qr')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Incidencia',
            fields=[
                ('idIncidencia', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('incidencia', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('idAlerta', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('1', 'Pendiente'), ('2', 'Resuelto')], default='1', max_length=1)),
                ('fecha', models.DateField()),
                ('evidencia', models.ImageField(upload_to='')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.departamento')),
                ('tipo_incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.tipo_incidencia')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.departamento')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.rol')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
