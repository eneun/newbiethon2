# Generated by Django 2.2.1 on 2019-05-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nore', '0004_room_norebang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='norebang',
            field=models.CharField(choices=[('1', '수노래방'), ('2', '라이브노래방'), ('3', '딩기딩기노래방'), ('4', '씽씽노래방')], max_length=30),
        ),
    ]
