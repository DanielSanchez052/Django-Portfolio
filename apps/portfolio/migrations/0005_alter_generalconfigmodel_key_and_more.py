# Generated by Django 4.1.3 on 2022-11-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_generalconfigmodel_key_section_contraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfigmodel',
            name='key',
            field=models.CharField(max_length=255, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='generalconfigmodel',
            name='section',
            field=models.CharField(max_length=150, verbose_name='section'),
        ),
        migrations.AlterField(
            model_name='generalconfigmodel',
            name='value',
            field=models.TextField(verbose_name='value'),
        ),
    ]
