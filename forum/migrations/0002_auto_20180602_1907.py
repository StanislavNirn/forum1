# Generated by Django 2.0.4 on 2018-06-02 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='topico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Topico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topico',
            name='titulo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
