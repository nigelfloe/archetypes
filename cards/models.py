from autoslug import AutoSlugField

from django.db import models
from django.template.defaultfilters import slugify


def generate_slug(card):
    return f'{card.deck}-{slugify(card.name)}'


class Archetype(models.Model):
    def __str__(self):
        return f'{self.pk}'


class Card(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE)
    deck = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from=generate_slug, unique_with=('deck', 'name'))
    suit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.deck}: {self.name}'

    @property
    def split_slug(self):
        return self.slug.split('-', maxsplit=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self)
        super().save(*args, **kwargs)
