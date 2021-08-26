from django.shortcuts import render
from django.core import serializers
import random

from .models import Story


def index(request):
    stories = list(Story.objects.values())
    random_story = random.choice(stories)
    template = 'structure_gen/index.html'
    context = {
        'stories': stories,
        'random_story': random_story,
    }

    return render(request, template, context)
