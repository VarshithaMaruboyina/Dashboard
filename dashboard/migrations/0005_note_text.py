# Generated by Django 3.0.5 on 2021-05-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_note_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.CharField(default='NULL', max_length=1000),
            preserve_default=False,
        ),
    ]
