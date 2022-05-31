# Generated by Django 4.0.4 on 2022-05-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_item_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]
