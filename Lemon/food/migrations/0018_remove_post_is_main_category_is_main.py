# Generated by Django 4.1.1 on 2022-10-05 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_post_is_main_alter_poststep_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_main',
        ),
        migrations.AddField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='На главной'),
        ),
    ]
