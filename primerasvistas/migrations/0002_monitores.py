from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
