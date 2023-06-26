# Generated by Django 4.1 on 2023-06-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_profile_player_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='player_type',
            field=models.CharField(blank=True, choices=[('xiuxian', '休闲'), ('yeren', '野人')], max_length=20, null=True),
        ),
    ]