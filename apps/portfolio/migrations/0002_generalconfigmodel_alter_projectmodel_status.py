# Generated by Django 4.1.3 on 2022-11-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=500)),
                ('section', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'General Config',
                'verbose_name_plural': 'General Config',
            },
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='status',
            field=models.CharField(choices=[('CP', 'COMPLETO'), ('PA', 'PAUSADO'), ('IN', 'INCOMPLETO'), ('IP', 'EN PROCESO')], default='IP', max_length=2),
        ),
    ]
