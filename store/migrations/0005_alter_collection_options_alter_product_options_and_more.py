# Generated by Django 5.2.1 on 2025-06-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20250525_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(null=True, to='store.promotion'),
        ),
    ]
