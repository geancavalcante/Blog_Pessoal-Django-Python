# Generated by Django 5.0.7 on 2024-08-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0015_remove_posting_book_remove_posting_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]