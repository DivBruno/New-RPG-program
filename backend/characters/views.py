from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Attributes

def index(request):
    attributes_list = Attributes.objects.order_by("-strength")[:3]
    context = {"attributes_list": attributes_list}
    return render(request, "characters/index.html", context)

def detail(request, attributes_id):
    try: 
        attribute = Attributes.objects.get(pk = attributes_id)
    except Attributes.DoesNotExist:
        raise Http404("Womp Womp. Attribute does not exist")
    return render(request, "characters/detail.html", {"attribute": attribute})
    # return HttpResponse("looking at the attributes %s." % Attributes.objects.get(pk = attributes_id))

def upgrade(request, attributes_id):
    return HttpResponse("upgrading the attributes %s." % Attributes.objects.get(pk = attributes_id))