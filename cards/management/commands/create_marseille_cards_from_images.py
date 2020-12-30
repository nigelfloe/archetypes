import os
import re

from django.core.management.base import BaseCommand
from cards.models import Archetype, Card

STATIC_PREFIX = 'cards/static'

MINOR_SUIT_RANKS = {
    'Ace': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    'Page': '11',
    'Knight': '12',
    'Queen': '13',
    'King': '14'
}

class Command(BaseCommand):
    help = 'Creates Marseille cards in DB from images in static/marseille'

    def handle(self, *args, **options):
        for filename in  os.listdir('cards/static/marseille'):
            image = f'marseille/{filename}'
            major_match = re.match(r'^(Card (\d{1,2})(: (.+))?|The Fool)\.jpg$', filename)
            minor_match = re.match(r'^((\w{1,6}) of (\w{4,6}))\.jpg$', filename)
            if major_match:
                name = major_match.group(4)
                rank = major_match.group(2)
                suit = 'Major'
                if not name:
                    if not rank:
                        name = 'The Fool'
                        rank = '[22]'
                    else:
                        name = '[Death]'

            if minor_match:
                name = minor_match.group(1)
                rank = MINOR_SUIT_RANKS[minor_match.group(2)]
                suit = minor_match.group(3)

            archetype = Archetype.objects.create()
            print(filename, name)
            Card.objects.create(
                archetype=archetype,
                deck='Marseille',
                image=image,
                name=name,
                rank=rank,
                suit=suit
            )
