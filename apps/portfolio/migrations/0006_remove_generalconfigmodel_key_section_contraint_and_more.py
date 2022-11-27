# Generated by Django 4.1.3 on 2022-11-26 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_generalconfigmodel_key_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='generalconfigmodel',
            name='key_section_contraint',
        ),
        migrations.AlterUniqueTogether(
            name='generalconfigmodel',
            unique_together={('key', 'section')},
        ),
    ]
