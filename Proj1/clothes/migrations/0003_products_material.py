# Generated by Django 3.1.1 on 2020-10-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Material',
            field=models.CharField(choices=[('S', 'Silk'), ('C', 'Cotton')], default='C', max_length=100),
        ),
    ]