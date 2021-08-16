from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'structure_gen/index.html'
    context = {
        
    }

    return render(request, template, context)
