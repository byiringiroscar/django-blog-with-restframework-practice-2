# Generated by Django 3.1.4 on 2021-11-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
