# Generated by Django 5.0.7 on 2024-08-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0005_alter_books_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='text_conclusion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_development',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_introdution',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
