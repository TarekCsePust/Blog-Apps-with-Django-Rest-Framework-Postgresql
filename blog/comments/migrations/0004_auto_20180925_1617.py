# Generated by Django 2.0.7 on 2018-09-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
    ]