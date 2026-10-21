from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Attributes, Character

def index(request):
    characters_list = Character.objects.order_by("-level")
    context = {"characters_list": characters_list}
    return render(request, "characters/index.html", context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk = character_id)
    attributes_list = character.attributes.get_attributes()
    return render(request, "characters/detail.html", {"character": character, "attributes_list": attributes_list.items()})

def upgrade(request, character_id):
    character = get_object_or_404(Character, pk = character_id)
    
    choice = request.POST.get("choice")
    attributes = character.attributes

    if choice in attributes.get_attributes():
        current_level = getattr(attributes, choice)
        setattr(attributes, choice, current_level + 1)
        attributes.save()

        messages.success(request, f"Atributo {choice} aumentado de {current_level} para {current_level + 1} com sucesso!")
    else:
        messages.error(request, "Escolha um atributo!")
    
    return HttpResponseRedirect(reverse("characters:detail", args=(character.id,)))

def downgrade(request, character_id):
    character = get_object_or_404(Character, pk = character_id)

    choice = request.POST.get("choice")
    attributes = character.attributes

    if choice in attributes.get_attributes():
        current_level = getattr(attributes, choice)
        setattr(attributes, choice, current_level - 1)
        attributes.save()

        messages.success(request, f"Atributo {choice} diminuido de {current_level} para {current_level - 1} com sucesso!")
    else:
        messages.error(request, "Escolha um atributo!")

    return HttpResponseRedirect(reverse("characters:detail", args=(character.id,)))


def create(request):
    char = Character()
    char.random_create()

    return HttpResponse("Character created.")