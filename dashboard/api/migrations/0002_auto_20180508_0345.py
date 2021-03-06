# Generated by Django 2.0.5 on 2018-05-08 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlement',
            name='carrier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Carrier'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='carrier',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='carrier',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='carrier',
            name='settlement',
        ),
    ]
