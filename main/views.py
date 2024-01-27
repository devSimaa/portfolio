from django.shortcuts import render

def index (request):
    context = {
        'name': 'Home'
    }
    return render(request, 'main/index.html', context)
