from django.shortcuts import render

def index(req):
    dict = {
        'index_header' : 'FPT Software'
    }
    return render(req, 'first_app/index.html', context=dict)
