from django.shortcuts import render


def index(request):
    data = {'title': 'shopping cart'}
    return render(request, 'clinic/index.html', context=data)


def cart(request):
    data = {'title': 'shopping cart'}
    return render(request, 'clinic/cart.html', context=data)


def checkout(request):
    data = {'title': 'check cart'}
    return render(request, 'clinic/checkout.html', context=data)

