# Generated by Django 3.1.7 on 2021-06-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20210604_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=5, null=True),
        ),
    ]
