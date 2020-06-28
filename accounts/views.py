from django.shortcuts import render



def sign_up(request):
    data = {'title': 'Registration'}
    return render(request, 'accounts/sign_up.html', context=data)


def sign_in(request):
    data = {'title': 'Authorization'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'log out'}
    return render(request, 'accounts/sign_out.html', context=data)
