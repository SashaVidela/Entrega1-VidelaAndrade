# Generated by Django 4.0.5 on 2022-07-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0005_celulares_avatars_alter_celulares_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celulares',
            name='avatars',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
