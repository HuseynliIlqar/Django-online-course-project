# Generated by Django 5.2 on 2025-04-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_teachers_read_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='UPDATE_FONT_AWESOME',
            field=models.CharField(default='', max_length=200),
        ),
    ]
