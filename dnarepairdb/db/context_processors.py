from .models import Pathway
from django.template import RequestContext


def get_pathways_processor(request):

    all_pathways = Pathway.objects.all()
    return {'all_pathways': all_pathways}