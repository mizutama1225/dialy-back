# Generated by Django 5.1.1 on 2024-09-20 04:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writtenletter', '0003_alter_writtenletter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writtenletter',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
