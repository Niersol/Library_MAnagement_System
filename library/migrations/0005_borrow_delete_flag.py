# Generated by Django 5.0.1 on 2024-01-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_books_borrow_category_students_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
    ]
