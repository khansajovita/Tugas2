# Generated by Django 4.1 on 2022-09-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MywatchlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('release_date', models.CharField(max_length=100)),
                ('review', models.TextField()),
            ],
        ),
    ]
