# Generated by Django 5.0.7 on 2024-08-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0007_alter_books_book_alter_posting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_conclusion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_development',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posting',
            name='text_introdution',
            field=models.TextField(),
        ),
    ]
