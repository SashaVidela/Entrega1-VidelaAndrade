from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0002_monitores'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Monitores',
        ),
    ]
