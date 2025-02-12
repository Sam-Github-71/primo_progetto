import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('descrizione', models.TextField()),
                ('data_inizio', models.DateField()),
                ('data_fine', models.DateField()),
                ('posti_disponibili', models.IntegerField()),
            ],
        ),
    ]


