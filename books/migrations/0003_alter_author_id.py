# Generated by Django 4.2.9 on 2024-01-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
    ]
