# Generated by Django 3.1 on 2020-08-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20200826_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignedTo',
            field=models.CharField(default='NONE', max_length=240),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='completedBy',
            field=models.CharField(default='NONE', max_length=240),
        ),
    ]
