# Generated by Django 3.2 on 2021-05-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlApp', '0006_auto_20210520_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='option',
            field=models.CharField(choices=[('1', 'Begin'), ('2', 'Loop')], default='1', max_length=2),
        ),
    ]