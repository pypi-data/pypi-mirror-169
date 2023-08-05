# Generated by Django 3.2.8 on 2022-01-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0059_invtypematerials_met_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeOzoneLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('station_id', models.CharField(max_length=500)),
                ('quantity', models.BigIntegerField()),
                ('used', models.BigIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
