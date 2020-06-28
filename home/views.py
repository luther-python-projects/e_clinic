from django.shortcuts import render


def index(request):
    data = {'title': 'main'}
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'about the site'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = {'title': 'contact'}
    return render(request, 'home/contacts.html', context=data)
