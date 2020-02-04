# Generated by Django 2.1 on 2020-01-27 16:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chemical_space', '0003_descriptors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FP',
        ),
        migrations.DeleteModel(
            name='PP',
        ),
        migrations.AlterField(
            model_name='descriptors',
            name='pca_fp',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MACCS Keys', 'MACCS Keys'), ('ECFP 4', 'ECFP 4'), ('ECFP 6', 'ECFP6')], max_length=24, verbose_name='Fingerprint'),
        ),
        migrations.AlterField(
            model_name='descriptors',
            name='pca_pp',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Physicochemical properties', 'Physicochemical properties')], max_length=26, verbose_name='Phisicochemical'),
        ),
        migrations.AlterField(
            model_name='descriptors',
            name='tsne_fp',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MACCS Keys', 'MACCS Keys'), ('ECFP 4', 'ECFP 4'), ('ECFP 6', 'ECFP6')], max_length=24, verbose_name='Fingerprint'),
        ),
        migrations.AlterField(
            model_name='descriptors',
            name='tsne_pp',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Physicochemical properties', 'Physicochemical properties')], max_length=26, verbose_name='Phisicochemical'),
        ),
    ]