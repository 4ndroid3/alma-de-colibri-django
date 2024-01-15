from django.shortcuts import render

def index(request):
    context = {
        'saranda': 'saras',
        'gaspacho': 31
    }
    return render(request, 'base/index.html', context=context)