# from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')


def contact_view(request):
    # return HttpResponse('contactez nous')
    return render(request, 'contact.html')


def articles_view(request):
    return render(request, 'articles.html')

# def login_view(request):
#     return render(request, 'login.html')
