# Generated by Django 2.2 on 2019-04-22 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='invitedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Member'),
        ),
    ]
