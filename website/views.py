from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
      lista = [
            'Django', 'Python', 'Git', 'Html', 
            'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi',
            'Systemclt'
      ]
      data ={'name': 'Curso de Django 3', 'lista_tecnologias':lista}
      return render(request, 'index.html', data)

    # return render(request, 'indexgeral.html')
    #return HttpResponse('Blog')