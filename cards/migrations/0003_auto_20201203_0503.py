# Generated by Django 3.1.4 on 2020-12-03 05:03

import autoslug.fields
import cards.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=cards.models.generate_card_slug, unique_with=('deck', 'name')),
        ),
    ]
