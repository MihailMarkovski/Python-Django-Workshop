# Generated by Django 3.2 on 2021-05-20 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[['dog', 'Dog'], ['cat', 'Cat'], ['parrot', 'Parrot'], ['unknown', 'Unknown']], default='unknown', max_length=50)),
                ('name', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pets.pet')),
            ],
        ),
    ]
