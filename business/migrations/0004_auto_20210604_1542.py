# Generated by Django 3.1.7 on 2021-06-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=5, null=True),
        ),
    ]
