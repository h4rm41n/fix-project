# Generated by Django 2.1.5 on 2019-03-14 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tps', '0003_auto_20190314_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tps',
            options={'ordering': ['kecamatan']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='tps',
            order_with_respect_to=None,
        ),
    ]