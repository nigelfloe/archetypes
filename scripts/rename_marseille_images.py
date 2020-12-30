#!/usr/bin/env python3
import os
import re
import shutil

STATIC_PREFIX = 'cards/static'
SOURCE_PREFIX = f'{STATIC_PREFIX}/cards'

SUIT_TRANSLATION = {
    'a': 'Major',
    'b': 'Wands',
    'c': 'Cups',
    'd': 'Coins',
    'e': 'Swords'
}

MAJOR_SUIT_NAMES = {
    '01': 'The Magician',
    '02': 'The Popess',
    '03': 'The Empress',
    '04': 'The Emperor',
    '05': 'The Pope',
    '06': 'The Lover',
    '07': 'The Chariot',
    '08': 'Justice',
    '09': 'The Hermit',
    '10': 'The Wheel of Fortune',
    '11': 'Force',
    '12': 'The Hanged Man',
    '13': '',
    '14': 'Temperance',
    '15': 'The Devil',
    '16': 'The Tower',
    '17': 'The Star',
    '18': 'The Moon',
    '19': 'The Sun',
    '20': 'Judgment',
    '21': 'The World',
    '22': 'The Fool'
}

MINOR_SUIT_NAMES = {
    '01': 'Ace',
    '02': '2',
    '03': '3',
    '04': '4',
    '05': '5',
    '06': '6',
    '07': '7',
    '08': '8',
    '09': '9',
    '10': '10',
    '11': 'Page',
    '12': 'Knight',
    '13': 'Queen',
    '14': 'King'
}

if __name__ == "__main__":
    for filename in os.listdir(SOURCE_PREFIX):
        suit_code, rank = re.match(r'^([a-z])(\d{2}).jpg$', filename).groups()
        suit = SUIT_TRANSLATION.get(suit_code)
        if suit:
            if suit == 'Major':
                rank_string = f'Card {int(rank)}'
                card_name = MAJOR_SUIT_NAMES[rank]
                if card_name:
                    if card_name == 'The Fool':
                        full_card_name = card_name
                    else:
                        full_card_name = f'{rank_string}: {card_name}'
                else:
                    full_card_name = rank_string
            else:
                full_card_name = f'{MINOR_SUIT_NAMES[rank]} of {suit}'
            og_filepath = f'{SOURCE_PREFIX}/{filename}'
            new_filepath = f'{STATIC_PREFIX}/marseille/{full_card_name}.jpg'
            print(f'Copying {og_filepath} to {new_filepath}')
            shutil.copy(og_filepath, new_filepath)
