# Generated by Django 4.1 on 2023-06-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_event_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.CharField(choices=[('1', '1'), ('1.5', 'yidianwu')], max_length=10, null=True),
        ),
    ]