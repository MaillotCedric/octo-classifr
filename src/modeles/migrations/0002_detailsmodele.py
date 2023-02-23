# Generated by Django 4.1.7 on 2023-02-23 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_images', '0001_initial'),
        ('modeles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailsmodele',
            fields=[
                ('id_modele', models.OneToOneField(db_column='id_modele', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='modeles.modele')),
                ('id_categorie', models.ForeignKey(db_column='id_categorie', on_delete=django.db.models.deletion.DO_NOTHING, to='app_images.categorie')),
            ],
            options={
                'db_table': 'detailsmodele',
                'managed': True,
                'unique_together': {('id_modele', 'id_categorie')},
            },
        ),
    ]
