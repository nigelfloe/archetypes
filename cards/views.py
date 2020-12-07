import logging

from django.views import generic

from .models import Archetype, Card

logger = logging.getLogger('root')


class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'archetype_list'

    def get_queryset(self):
        return Archetype.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['siblings'] = self.object.archetype.card_set.exclude(deck=self.object.deck)
        return context
