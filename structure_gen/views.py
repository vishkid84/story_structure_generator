from django.shortcuts import render
from django.core import serializers
import random

from .models import Story
from .forms import StoryForm


def home(request):
    stories = list(Story.objects.values())
    random_story = random.choice(stories)

    if request.method == 'POST':
        form = StoryForm(request.POST or None)
        if form.is_valid:
            story = form.save()
            story.name = random_story.name
            story.save()
            return redirect(reverse('home'))

    else:
        form = StoryForm()

    template = 'structure_gen/index.html'
    context = {
        'stories': stories,
        'random_story': random_story,
        'form': form,
    }

    return render(request, template, context)
