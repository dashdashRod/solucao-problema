from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint


# [100, 470, 400, 520, 600, 600, 600]


#Dados mocados

data = { 
    'cerais1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'cerais2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'cerais3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'milho1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'milho2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'milho3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'vegetais1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'vegetais2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'vegetais3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    
    'shirt1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'shirt2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'shirt3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'casaco1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'casaco2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'casaco3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'oculos1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'oculos2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'oculos3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    
    'carros1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'carros2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'carros3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'motos1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'motos2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'motos3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'caminhao1': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'caminhao2': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    'caminhao3': [randint(0,600),randint(0,600),randint(0,600),randint(0,600),600, 600, 600],
    
}

@csrf_exempt
def home(request):
    r = {}
    if (request.method == 'GET'):
        r = JsonResponse(data=data)
    return r

def second_home(request):
    posts = {

    }
    context = {
        'posts': posts
    }
    return render(request,'blog/index.html',context=context) 

# Create your views here.
