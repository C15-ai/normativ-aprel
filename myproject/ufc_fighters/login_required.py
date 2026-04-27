from django.shortcuts import render, redirect


def login_required(func):
    def wrapper(request , *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper
