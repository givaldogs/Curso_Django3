from django.shortcuts import render
from .models import Post

# Create your views here.

def hello_blog(request):
      list = [
            'Django', 'Python', 'Git', 'Html', 
            'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi',
            'Systemclt'
      ]
      list_posts = Post.objects.all()
      data ={'name': 'Curso de Django 3', 'lista_tecnologias':list,
             'posts': list_posts
             }
      return render(request, 'index.html', data)

    # return render(request, 'indexgeral.html')
    #return HttpResponse('Blog')
