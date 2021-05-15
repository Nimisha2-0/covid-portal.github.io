# Generated by Django 3.2.1 on 2021-05-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(blank=True, choices=[('W', 'Waiting'), ('A', 'Admitted'), ('D', 'Discharged')], default='W', max_length=2),
        ),
    ]
