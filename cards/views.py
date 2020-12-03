import logging

from django.shortcuts import get_object_or_404, render

from .models import Archetype, Card

logger = logging.getLogger('root')


def index(request):
    archetype_list = Archetype.objects.order_by('id')
    context = {'archetype_list': archetype_list}
    return render(request, 'cards/index.html', context)


def detail(request, deck, name):
    card = get_object_or_404(Card, slug=f'{deck}-{name}')
    return render(request, 'cards/detail.html', {'card': card})
