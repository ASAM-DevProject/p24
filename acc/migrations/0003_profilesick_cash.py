# Generated by Django 4.0.1 on 2022-01-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilesick',
            name='cash',
            field=models.IntegerField(blank=True, null=True, verbose_name='موجودی'),
        ),
    ]
