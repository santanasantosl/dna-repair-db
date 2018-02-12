from .models import Pathway, Organism
from django.template import RequestContext


def get_pathways_processor(request):

    all_pathways = Pathway.objects.all()
    return {'all_pathways': all_pathways}


def get_organisms_processor(request):

    all_organisms = Organism.objects.all().order_by('abbreviation')
    return {'all_organisms': all_organisms}