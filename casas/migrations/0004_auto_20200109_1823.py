# Generated by Django 3.0.2 on 2020-01-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_remove_pessoa_casa'),
        ('casas', '0003_auto_20200109_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casa',
            name='dono',
        ),
        migrations.AddField(
            model_name='casa',
            name='dono',
            field=models.ManyToManyField(blank=True, null=True, to='pessoas.Pessoa'),
        ),
    ]
