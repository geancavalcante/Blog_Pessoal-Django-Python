# Generated by Django 5.0.7 on 2024-08-01 19:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0024_alter_books_book_alter_books_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='text_conclusion',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_development',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_introdution',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
