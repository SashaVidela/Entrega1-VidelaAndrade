# Generated by Django 4.0.5 on 2022-07-25 19:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0004_celulares_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='celulares',
            name='avatars',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='celulares',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
