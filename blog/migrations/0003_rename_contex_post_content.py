# Generated by Django 4.2 on 2025-04-10 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_view_post_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contex',
            new_name='content',
        ),
    ]
