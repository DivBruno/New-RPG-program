from django.http import HttpResponse
from django.template import loader
from .models import Attributes

def index(request):
    attributes_list = Attributes.objects.order_by("-strength")[:3]
    template = loader.get_template("characters/index.html")
    context = {"attributes_list": attributes_list}
    return HttpResponse(template.render(context))

def detail(request, attributes_id):
    return HttpResponse("looking at the attributes %s." % Attributes.objects.get(pk = attributes_id))

def upgrade(request, attributes_id):
    return HttpResponse("upgrading the attributes %s." % Attributes.objects.get(pk = attributes_id))