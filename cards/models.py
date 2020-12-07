from autoslug import AutoSlugField

from django.db import models
from django.template.defaultfilters import slugify


def generate_card_slug(card):
    return f'{card.deck}/{slugify(card.name)}'


def hierarchical_slugify(slug, separator='/'):
    return separator.join([slugify(level) for level in slug.split(separator)])


class Archetype(models.Model):
    def __str__(self):
        return f'{self.pk}'


class Card(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE)
    deck = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=10)
    slug = AutoSlugField(
        always_update=True,
        populate_from=generate_card_slug,
        unique_with=('deck', 'name'),
        slugify=hierarchical_slugify
    )
    suit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.deck}: {self.name}'

    @property
    def split_slug(self):
        return self.slug.split('-', maxsplit=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_card_slug(self)
        super().save(*args, **kwargs)
