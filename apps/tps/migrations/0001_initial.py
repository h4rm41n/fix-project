# Generated by Django 2.1.5 on 2019-03-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kecamatan', models.CharField(blank=True, max_length=100, null=True)),
                ('kelurahan', models.CharField(blank=True, max_length=100, null=True)),
                ('lingkungan', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]