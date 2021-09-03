# Generated by Django 3.2.5 on 2021-08-31 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[['dog', 'Dog'], ['cat', 'Cat'], ['parrot', 'Parrot'], ['rabbit', 'Rabbit'], ['unknown', 'Unknown']], default='unknown', max_length=50),
        ),
    ]
