import json

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.cache import never_cache

from models import Ortholog


@never_cache
def search_nav(request):
    JsonObject = {
        'sucess': False,
        'message': '',
    }

    if request.method == "GET":

        q = request.GET.get('q', None)
        JsonObject['q'] = q

        empty = True

        q = q.strip()
        if q:
            qq = [q]
            ortholog = Ortholog.objects.filter(symbol__icontains=qq[0]).values('id', 'symbol')
            empty = not(ortholog.exists())
        pass

        if request.is_ajax():
            JsonObject['success'] = True
            JsonObject['message'] = "Records found."
            #
            JsonObject['ortholog'] = json.dumps([o for o in ortholog])
            JsonObject['empty'] = empty
            pass
        else:
            JsonObject['message'] = "Non-AJAX call received"
            pass
        pass
    else:
        JsonObject['message'] = "unsupported method '{m}'".format(m=request.method)
        pass
    return JsonResponse(JsonObject)