# Generated by Django 3.1.2 on 2022-06-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='decmats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('n', models.IntegerField()),
                ('d', models.IntegerField()),
                ('blocklabels', models.TextField()),
                ('blocks', models.TextField()),
                ('condition', models.TextField()),
                ('decmat', models.TextField()),
                ('hc_series', models.TextField()),
                ('ordinary', models.TextField()),
                ('origin', models.TextField()),
                ('recipe', models.TextField()),
            ],
        ),
    ]
