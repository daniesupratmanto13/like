# Generated by Django 3.1.2 on 2020-12-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_auto_20201211_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
