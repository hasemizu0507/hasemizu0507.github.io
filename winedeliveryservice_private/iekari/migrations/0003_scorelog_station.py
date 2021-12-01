# Generated by Django 2.2.1 on 2021-08-25 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iekari', '0002_rentroom_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='駅ID')),
                ('name', models.CharField(max_length=50, verbose_name='駅名')),
                ('latitude', models.FloatField(verbose_name='駅緯度')),
                ('longitude', models.FloatField(verbose_name='駅経度')),
            ],
            options={
                'verbose_name': '駅データ',
                'verbose_name_plural': '駅データ',
            },
        ),
        migrations.CreateModel(
            name='ScoreLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='評価')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='日時')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iekari.Profile', verbose_name='ユーザー情報')),
                ('rent_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iekari.RentRoom', verbose_name='物件')),
            ],
            options={
                'verbose_name': '賃貸物件評価データ',
                'verbose_name_plural': '賃貸物件評価データ',
            },
        ),
    ]
