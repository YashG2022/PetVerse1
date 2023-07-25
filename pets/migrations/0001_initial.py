# Generated by Django 4.2.3 on 2023-07-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pets',
            fields=[
                ('petidnumber', models.AutoField(primary_key=True, serialize=False)),
                ('species', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('birth_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]