from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    template = 'structure_gen/structure_gen.html'
    context = {
        
    }

    return render(request, template, context)
    