# Generated by Django 4.2 on 2023-04-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]