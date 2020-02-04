# Generated by Django 2.1 on 2020-01-21 20:42

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Build', '0004_auto_20200121_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFormulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', multiselectfield.db.fields.MultiSelectField(choices=[('ALA', 'ALA'), ('CYS', 'CYS'), ('ASP', 'ASP'), ('GLU', 'GLU'), ('PHE', 'PHE'), ('HIS', 'HIS'), ('ILE', 'ILE'), ('LYS', 'LYS'), ('LEU', 'LEU'), ('MET', 'MET'), ('ASN', 'ASN'), ('PRO', 'PRO'), ('GLN', 'GLN'), ('ARG', 'ARG'), ('SER', 'SER'), ('THR', 'THR'), ('VAL', 'VAL'), ('TRP', 'TRP'), ('TYR', 'TYR'), ('GLY', 'GLY')], max_length=79, verbose_name='First position')),
                ('linear', multiselectfield.db.fields.MultiSelectField(choices=[('ALA', 'ALA'), ('CYS', 'CYS'), ('ASP', 'ASP'), ('GLU', 'GLU'), ('PHE', 'PHE'), ('HIS', 'HIS'), ('ILE', 'ILE'), ('LYS', 'LYS'), ('LEU', 'LEU'), ('MET', 'MET'), ('ASN', 'ASN'), ('PRO', 'PRO'), ('GLN', 'GLN'), ('ARG', 'ARG'), ('SER', 'SER'), ('THR', 'THR'), ('VAL', 'VAL'), ('TRP', 'TRP'), ('TYR', 'TYR'), ('GLY', 'GLY')], max_length=79, verbose_name='Linear')),
                ('methylated', multiselectfield.db.fields.MultiSelectField(choices=[('ALA', 'ALA'), ('CYS', 'CYS'), ('ASP', 'ASP'), ('GLU', 'GLU'), ('PHE', 'PHE'), ('HIS', 'HIS'), ('ILE', 'ILE'), ('LYS', 'LYS'), ('LEU', 'LEU'), ('MET', 'MET'), ('ASN', 'ASN'), ('PRO', 'PRO'), ('GLN', 'GLN'), ('ARG', 'ARG'), ('SER', 'SER'), ('THR', 'THR'), ('VAL', 'VAL'), ('TRP', 'TRP'), ('TYR', 'TYR'), ('GLY', 'GLY')], max_length=79, verbose_name='Methylated')),
                ('topology', multiselectfield.db.fields.MultiSelectField(choices=[('linear', 'linear'), ('cyclic', 'cyclic')], max_length=13, verbose_name='Topology')),
                ('length', models.IntegerField(verbose_name='Length')),
            ],
        ),
        migrations.DeleteModel(
            name='Linear',
        ),
        migrations.DeleteModel(
            name='Methylated',
        ),
    ]
