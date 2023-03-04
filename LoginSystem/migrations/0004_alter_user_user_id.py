# Generated by Django 3.2.16 on 2022-12-20 15:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0003_auto_20221220_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('4a175fc5-1a20-4738-8547-77432e5fde9d'), editable=False, primary_key=True, serialize=False),
        ),
    ]