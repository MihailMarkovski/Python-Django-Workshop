# Generated by Django 3.2.5 on 2021-07-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
