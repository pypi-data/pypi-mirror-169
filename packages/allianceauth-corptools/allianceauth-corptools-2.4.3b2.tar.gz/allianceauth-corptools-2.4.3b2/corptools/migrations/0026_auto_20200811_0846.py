# Generated by Django 2.2.12 on 2020-08-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0025_mapjumpbridge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapjumpbridge',
            name='structure_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
