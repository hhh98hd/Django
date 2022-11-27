from django.shortcuts import render

def index(req):
    dict = {
        'index_header' : 'This is H1 header'
    }
    return render(req, 'first_app/index.html', context=dict)
