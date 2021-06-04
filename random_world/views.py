# Create your views here.
from django.http import request
from django.shortcuts import render, HttpResponse,  redirect
from django.utils.crypto import get_random_string

def index(request):
    return redirect("/random_word")

def random(request):
    if 'conteo' not in request.session:
        request.session['conteo'] = 0
    
    request.session['conteo'] += 1
    random = get_random_string(length=14)
    context = {
        'random':random
    }
    return render(request,'index.html',context)


def reset(request):
    del request.session['conteo']
    return redirect("/random_word")