# Generated by Django 2.1 on 2020-01-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Build', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='first',
            field=models.CharField(choices=[('ALA', 'ALA'), ('CYS', 'CYS'), ('ASP', 'ASP'), ('GLU', 'GLU'), ('PHE', 'PHE'), ('HIS', 'HIS'), ('ILE', 'ILE'), ('LYS', 'LYS'), ('LEU', 'LEU'), ('MET', 'MET'), ('ASN', 'ASN'), ('PRO', 'PRO'), ('GLN', 'GLN'), ('ARG', 'ARG'), ('SER', 'SER'), ('THR', 'THR'), ('VAL', 'VAL'), ('TRP', 'TRP'), ('TYR', 'TYR'), ('GLY', 'GLY')], max_length=1, verbose_name='First position'),
        ),
        migrations.AlterField(
            model_name='topology',
            name='length',
            field=models.IntegerField(verbose_name='length'),
        ),
    ]
