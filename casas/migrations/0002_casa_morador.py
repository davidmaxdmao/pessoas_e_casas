# Generated by Django 3.0.2 on 2020-01-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_remove_pessoa_casa'),
        ('casas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='morador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa'),
        ),
    ]
