
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0003_delete_monitores'),
    ]

    operations = [
        migrations.AddField(
            model_name='celulares',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
