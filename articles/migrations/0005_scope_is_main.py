# Generated by Django 5.0 on 2023-12-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_article_alter_scope_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default='False'),
        ),
    ]
