# Generated by Django 4.2.4 on 2024-07-11 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='site_busca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='job.portal'),
        ),
    ]
