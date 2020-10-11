# Generated by Django 3.1.1 on 2020-10-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Civ',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('expansion', models.TextField()),
                ('army_type', models.TextField()),
                ('team_bonus', models.TextField()),
                ('civilization_bonus', models.ManyToManyField(related_name='_civ_civilization_bonus_+', to='civs.Civ')),
                ('unique_tech', models.ManyToManyField(related_name='_civ_unique_tech_+', to='civs.Civ')),
                ('unique_unit', models.ManyToManyField(related_name='_civ_unique_unit_+', to='civs.Civ')),
            ],
        ),
    ]
