# Generated by Django 2.1.5 on 2019-01-09 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clientexpenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('currency', models.CharField(blank=True, choices=[('USD', '$'), ('EUR', '&euro;'), ('INR', '&#8377;')], default='INR', max_length=3)),
            ],
        ),
    ]
